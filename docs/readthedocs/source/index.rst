BigDL Documentation
===========================

------

`BigDL <https://github.com/intel-analytics/BigDL/>`_ makes it easy for data scientists and data engineers to build end-to-end, distributed AI applications. The **BigDL 2.0** release combines the `original BigDL <https://github.com/intel-analytics/BigDL/tree/branch-0.14>`_ and `Analytics Zoo <https://github.com/intel-analytics/analytics-zoo>`_ projects, providing the following features:

* `DLlib <doc/DLlib/Overview/dllib.html>`_: distributed deep learning library for Apache Spark
* `Orca <doc/Orca/Overview/orca.html>`_: seamlessly scale out TensorFlow and PyTorch pipelines for distributed Big Data
* `RayOnSpark <doc/Ray/Overview/ray.html>`_: run Ray programs directly on Big Data clusters
* `Chronos <doc/Chronos/Overview/chronos.html>`_: scalable time series analysis using AutoML
* `PPML <doc/PPML/Overview/ppml.html>`_: privacy preserving big data analysis and machine learning (*experimental*)
* `Nano <doc/Nano/Overview/nano.html>`_: automatically accelerate TensorFlow and PyTorch pipelines by applying model CPU optimizations
-------


.. meta::
   :google-site-verification: hG9ocvSRSRTY5z8g6RLn97_tdJvYRx_tVGhNdtZZavM

.. toctree::
   :maxdepth: 1
   :caption: Quick Start

   doc/Orca/QuickStart/orca-tf-quickstart.md
   doc/Orca/QuickStart/orca-keras-quickstart.md
   doc/Orca/QuickStart/orca-tf2keras-quickstart.md
   doc/Orca/QuickStart/orca-pytorch-quickstart.md
   doc/Ray/QuickStart/ray-quickstart.md

.. toctree::
   :maxdepth: 1
   :caption: User Guide

   doc/UserGuide/python.md
   doc/UserGuide/scala.md
   doc/UserGuide/colab.md
   doc/UserGuide/docker.md
   doc/UserGuide/hadoop.md
   doc/UserGuide/k8s.md
   doc/UserGuide/databricks.md
   doc/UserGuide/develop.md

.. toctree::
   :maxdepth: 1
   :caption: Nano Overview

   doc/Nano/Overview/nano.md
   doc/Nano/Overview/windows_guide.md
   doc/Nano/QuickStart/pytorch_train.md
   doc/Nano/QuickStart/pytorch_inference.md
   doc/Nano/QuickStart/tensorflow_train.md
   doc/Nano/QuickStart/tensorflow_inference.md
   doc/Nano/QuickStart/hpo.md
   doc/Nano/Overview/known_issues.md
   doc/Nano/QuickStart/index.md

.. toctree::
   :maxdepth: 1
   :caption: DLlib Overview

   doc/DLlib/Overview/dllib.md
   doc/DLlib/Overview/keras-api.md
   doc/DLlib/Overview/nnframes.md

.. toctree::
   :maxdepth: 1
   :caption: Orca Overview

   doc/Orca/Overview/orca.md
   doc/Orca/Overview/orca-context.md
   doc/Orca/Overview/data-parallel-processing.md
   doc/Orca/Overview/distributed-training-inference.md
   doc/Orca/Overview/distributed-tuning.md
   doc/Ray/Overview/ray.md

.. toctree::
   :maxdepth: 1
   :caption: Chronos Overview

   doc/Chronos/Overview/chronos.md
   doc/Chronos/Overview/deep_dive.rst
   doc/Chronos/QuickStart/index.md
   doc/Chronos/Overview/chronos_known_issue.md

.. toctree::
   :maxdepth: 1
   :caption: PPML Overview

   doc/PPML/Overview/ppml.md
   doc/PPML/Overview/trusted_big_bata_analytics_and_ml.md
   doc/PPML/Overview/trusted_fl.md
   doc/PPML/QuickStart/build_kernel_with_sgx.md
   doc/PPML/QuickStart/deploy_intel_sgx_device_plugin_for_kubernetes.md
   doc/PPML/QuickStart/trusted-serving-on-k8s-guide.md
   doc/PPML/QuickStart/tpc-h_with_sparksql_on_k8s.md
   doc/PPML/QuickStart/tpc-ds_with_sparksql_on_k8s.md
   doc/PPML/Overview/azure_ppml.md

.. toctree::
   :maxdepth: 1
   :caption: Serving Overview

   doc/Serving/Overview/serving.md
   doc/Serving/QuickStart/serving-quickstart.md
   doc/Serving/ProgrammingGuide/serving-installation.md
   doc/Serving/ProgrammingGuide/serving-start.md
   doc/Serving/ProgrammingGuide/serving-inference.md
   doc/Serving/Example/example.md
   doc/Serving/FAQ/faq.md
   doc/Serving/FAQ/contribute-guide.md

.. toctree::
   :maxdepth: 1
   :caption: Common Use Case

   doc/Orca/QuickStart/orca-pytorch-distributed-quickstart.md
   doc/UseCase/spark-dataframe.md
   doc/UseCase/xshards-pandas.md
   doc/Orca/QuickStart/orca-autoestimator-pytorch-quickstart.md
   doc/Orca/QuickStart/orca-autoxgboost-quickstart.md

.. toctree::
   :maxdepth: 1
   :caption: Python API

   doc/PythonAPI/Orca/orca.rst
   doc/PythonAPI/Friesian/feature.rst
   doc/PythonAPI/Chronos/index.rst
   doc/PythonAPI/Nano/index.rst

.. toctree::
   :maxdepth: 1
   :caption: Real-World Application

   doc/Application/presentations.md
   doc/Application/blogs.md
   doc/Application/powered-by.md

