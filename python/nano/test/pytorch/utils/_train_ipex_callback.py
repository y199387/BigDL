#
# Copyright 2016 The BigDL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import torch
from logging import warning
from typing import Dict
from pytorch_lightning.callbacks import Callback
from pytorch_lightning.plugins.training_type import SingleDevicePlugin, DDPSpawnPlugin
from bigdl.nano.pytorch.utils import TORCH_VERSION_LESS_1_10
from pytorch_lightning.accelerators.cpu import CPUAccelerator


class CheckIPEXCallback(Callback):
    def on_train_start(self, trainer, pl_module):
        if TORCH_VERSION_LESS_1_10:
            from bigdl.nano.deps.ipex.version_1_9.ipex_accelerator_1_9 import IPEXAccelerator
            if not isinstance(trainer.accelerator, IPEXAccelerator):
                warning("CheckIPEXCallback is used, but ipex fail")
                return
            from bigdl.nano.deps.ipex.version_1_9.ipex_torchfunctional import RESTORE_TYPE
            def check_device(obj):
                if torch.is_tensor(obj):
                    if obj.device.type == 'xpu':
                        return True
                    return False
                if isinstance(obj, RESTORE_TYPE):
                    iter_keys = obj.keys() if isinstance(obj, Dict) else range(len(obj))
                    for k in iter_keys:
                        if isinstance(obj[k], RESTORE_TYPE):
                            if not check_device(obj[k]):
                                return False
                return True
            assert check_device(pl_module.state_dict())
        else:
            from bigdl.nano.deps.ipex.ipex_accelerator import IPEXAccelerator
            from pytorch_lightning.plugins import DDPSpawnPlugin
            if not (isinstance(trainer.accelerator, IPEXAccelerator) or isinstance(trainer.training_type_plugin, DDPSpawnPlugin) and hasattr(trainer.training_type_plugin, 'use_ipex') and trainer.training_type_plugin.use_ipex == True):
                warning("CheckIPEXCallback is used, but ipex fail")
                return
            from intel_extension_for_pytorch.nn.utils._model_convert import _LSTM
            from intel_extension_for_pytorch.nn.utils._weight_prepack import _IPEXConvNd, _IPEXLinear, _IPEXConvTransposeNd
            IPEX_LAYERS = (_LSTM, 
                           _IPEXConvNd,
                           _IPEXLinear,
                           _IPEXConvTransposeNd)
            IPEX_ATTR   = ('master_weight',
                           'weight_trail',
                           'master_bias',
                           'bias_trail')
            def check_ipex_layers(m):
                if isinstance(m, IPEX_LAYERS):
                    print("model is optimized by IPEX")
                    print(f"model contains layer {m}")
                    return True
                for attr in IPEX_ATTR:
                    if hasattr(m, attr):
                        return True
                for name, sub_m in m.named_children():
                    if check_ipex_layers(sub_m):
                        return True
                return False
            assert check_ipex_layers(pl_module)

