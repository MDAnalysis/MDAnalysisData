.. -*- coding: utf-8 -*-

============
 Installing
============

The package is pure Python and one can directly install the
`MDAnalysisData package`_ from the Python Package Index (PyPi) with
:program:`pip`:
	   
.. code-block:: bash

   pip install --upgrade MDAnalysisData


Alternatively, you can also install it with the `conda`_ package
manager:

.. code-block:: bash

   conda config --add channels conda-forge
   conda install mdanalysisdata

and to upgrade later   

.. code-block:: bash

   conda update mdanalysis		


.. note:: The package itself is small and initially does not install
          any datasets. However, the :ref:`data directory
          <managing-data>`, where datasets are cached, can grow to
          many gigabytes.

.. _`MDAnalysisData package`:
   https://pypi.org/project/MDAnalysisData/
.. _conda: https://conda.io/docs/
   
Installing from source
======================

Clone the repository with

.. code-block:: bash

   git clone https://github.com/MDAnalysis/MDAnalysisData.git

and install with :program:`pip`

.. code-block:: bash

   pip install MDAnalysisData/
