
.. -*- coding: utf-8 -*-

.. _usage:

=======
 Usage
=======

All datasets in :mod:`MDAnalysisData` are accessible via ``fetch_*``
functions in the :mod:`MDAnalysisData.datasets` module. Datasets are
organized in submodules by the type of simulations that they
represent.  The currently included datasets are:

.. currentmodule:: MDAnalysisData

.. autosummary::

   adk_equilibrium
   adk_transitions
   PEG_1chain
   ifabp_water
   nhaa_equilibrium
   yiip_equilibrium   
   vesicles
   CG_fiber

Accessing a dataset
===================

As an example, we can access the :ref:`AdK equilibrium dataset
<adk-equilibrium-dataset>` with the
:func:`~MDAnalysisData.adk_equilibrium.fetch_adk_equilibrium`
function::

    >>> from MDAnalysisData import datasets
    >>> adk = datasets.fetch_adk_equilibrium()

This will download the dataset from figshare (doi:
`10.6084/m9.figshare.5108170.v1
<https://doi.org/10.6084/m9.figshare.5108170.v1>`_) and unpack it into
a cache directory. This means that only the first time executing
:func:`~MDAnalysisData.adk_equilibrium.fetch_adk_equilibrium` will be
slow; at later times, the cached files will be used. The resulting
:class:`~MDAnalysisData.base.Bunch` object can be introspected for
what this dataset includes.  In particular, it features a
:attr:`~MDAnalysisData.base.Bunch.DESCR` attribute with a
human-readable description of the dataset::

    >>> print(adk.DESCR)

    AdK equilibrium trajectory dataset
    ==================================

    MD trajectory of apo adenylate kinase with CHARMM27 force field and
    simulated with explicit water and ions in NPT at 300 K and 1
    bar. Saved every 240 ps for a total of 1.004 µs. Produced on PSC
    Anton. The trajectory only contains the protein and all solvent
    stripped. Superimposed on the CORE domain of AdK by RMSD fitting.

    The topology is contained in the PSF file (CHARMM format). The
    trajectory is contained in the DCD file (CHARMM/NAMD format).

    Notes
    -----

    Data set characteristics:

     :size: 161 MB
     :number of frames:  4187
     :number of particles: 3341
     :creator: Sean Seyler
     :URL:  `10.6084/m9.figshare.5108170.v1 <https://doi.org/10.6084/m9.figshare.5108170.v1>`_
     :license: `CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/legalcode>`_
     :reference: [Seyler2017]_


    .. [Seyler2017]  Seyler, Sean; Beckstein, Oliver (2017): Molecular dynamics
	       trajectory for benchmarking
	       MDAnalysis. figshare. Fileset. doi:
	       `10.6084/m9.figshare.5108170.v1
	       <https://doi.org/10.6084/m9.figshare.5108170.v1>`_


The topology and trajectory files can be accessed::

    >>> print(adk.topology)
    >>> print(adk.trajectory)

and one can immediately load it into an :class:`MDAnalysis.Universe
<MDAnalysis.core.universe.Universe>`::

    >>> import MDAnalysis as mda
    >>> u = mda.Universe(adk.topology, adk.trajectory)


.. _managing-data:

Managing data
=============

When data is downloaded from a remote location, it is copied to a
local data directory and cached. Subsequently, the cached copy is
used. By default, data are locally stored in the **data directory**
``~/MDAnalysis_data`` (i.e., under the user's home directory).

The location of the data directiory can be changed by setting the
environment variable :envvar:`MDANALYSIS_DATA`, for instance

.. code-block:: bash

   export MDANALYSIS_DATA=/tmp/MDAnalysis_data

All ``fetch_*`` functions also have a keyword argument `data_home` that
can be used to set an alternative data directory.

The location of the data directory can be obtained with
:func:`MDAnalysisData.base.get_data_home`.

If a dataset or the whole data directory is removed then the data are
downloaded again when they are needed. If data are downloaded as
archives (zip or tar files) then both the archive and the unpacked
data are stored; removing the archive will trigger a re-download
because only the archive itself is checked with the checksum.

Only datasets that are needed are downloaded. However, the full data
directory can take up more than 2 GB of space. One may manually delete
subdirectories (e.g. data sets that are currently not needed) and the
whole data directory can we wiped (removed) with the function
:func:`MDAnalysisData.base.clear_data_home`.
