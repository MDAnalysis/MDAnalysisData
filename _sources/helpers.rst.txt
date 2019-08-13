.. _helpers:

=========
 Helpers
=========

A small number of functions and classes are included to help organize
the data.

.. currentmodule:: MDAnalysisData.base



For users
=========

.. autoclass:: Bunch
   :members:

.. autodata:: DEFAULT_DATADIR
	  
.. autofunction:: get_data_home

.. autofunction:: clear_data_home


For developers
==============

If you want to add your own dataset then you will likely use these
functions in your code.


.. autodata:: RemoteFileMetadata
   
.. autofunction:: _sha256

.. autofunction:: _fetch_remote		  

.. autofunction:: _read_description

		  
