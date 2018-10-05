.. -*- coding: utf-8 -*-
.. MDAnalysisData documentation master file,

=================================================================
 MDAnalysisData: MD data for testing, learning, and benchmarking
=================================================================

|zenodo| |PRwelcome|

:Release: |release|
:Date: |today|

**MDAnalysisData** is a collection of datasets from the field of
computational biophysics, with an emphasis on trajectories from
molecular dynamics (MD) simulations and the structure and dynamics of
biomolecules.

Data sets are stored at external stable URLs (e.g., on figshare_ ,
zenodo_, or DataDryad_) and not inside the :mod:`MDAnalysisData`
package. Instead, the :mod:`MDAnalysisData.datasets` provides a simple
interface to download, cache, and access these externally hosted data
sets.

The files can be easily used with MDAnalysis_ but the package is
standalone and can be used for any purpose, for instance, to
provide examples for workshops and classes, and, of course, to try out
other tools for analyzing simulations.

Datasets are released under an `open license`_ that conforms to the `Open
Definition 2.1`_ that allows free use, re-use, redistribution, modification,
separation, for any purpose and without a charge. All  code
can be found in the public GitHub repository `mdanalysis/MDAnalysisData`_.

This library is *under active development*. We use `semantic
versioning`_ to indicate clearly what kind of changes you may expect
between releases. Please raise any issues or questions in the
`Issue Tracker`_. `Contributions of data sets`_ and code in the form
of pull requests are very welcome.

.. |zenodo| image:: https://zenodo.org/badge/147885122.svg
    :alt: Zenodo DOI
    :scale: 100%
    :target: https://zenodo.org/badge/latestdoi/147885122

.. |PRwelcome| image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :alt: PRs welcome
   :target: http://makeapullrequest.com

.. _`MDAnalysis`: https://www.mdanalysis.org
.. _`mdanalysis/MDAnalysisData`: https://github.com/MDAnalysis/MDAnalysisData
.. _figshare: https://figshare.com/
.. _zenodo: https://zenodo.org/
.. _DataDryad: https://www.datadryad.org/
.. _`open license`:
   http://opendefinition.org/licenses/#recommended-conformant-licenses
.. _`Open Definition 2.1`: http://opendefinition.org/od/2.1/en/
.. _`semantic versioning`: https://semver.org   
.. _`Issue Tracker`:
   https://github.com/mdanalysis/MDAnalysisData/issues
.. _`Contributions of data sets`:
   https://github.com/mdanalysis/MDAnalysisData/wiki/contributing
   

.. toctree::
   :maxdepth: 2
   :caption: Overview
   :hidden:
	      
   install
   usage
   helpers
   credits

.. toctree::
   :maxdepth: 1
   :caption: Datasets
   :hidden:

   adk_equilibrium
   adk_transitions
   ifabp_water
   vesicles
