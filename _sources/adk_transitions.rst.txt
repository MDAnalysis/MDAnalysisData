.. -*- coding: utf-8 -*-

.. _adk-transitions:

==========================
 AdK transitions datasets
==========================

.. module:: MDAnalysisData.adk_transitions

The :mod:`MDAnalysisData.adk_transitions` module contains ensembles of
trajectories during which the close-to-open transiton of the enzyme
adenylate kinase [Seyler2014]_ is sampled using different
computational methods [Seyler2015]_.

   
.. currentmodule:: MDAnalysisData.adk_transitions

.. autosummary::

   fetch_adk_transitions_DIMS
   fetch_adk_transitions_FRODA   

.. SeeAlso:: This set of trajectories was used in the `SPIDAL
   Tutorial: MDAnalysis with Midas/radical.pilot`_ where the ensemble
   of 400 DIMS+FRODA trajectories is analyzed with the *Path
   Similarity Analysis* method [Seyler2015]_. Computations on such a
   large(ish) dataset are sped up by parallelization at the task level
   with `RADICAL-Pilot`_.

.. _`SPIDAL Tutorial: MDAnalysis with Midas/radical.pilot`:
   https://www.mdanalysis.org/SPIDAL-MDAnalysis-Midas-tutorial/
.. _`RADICAL-Pilot`: https://radical-cybertools.github.io/



.. include:: ../MDAnalysisData/descr/adk_transitions_DIMS.rst

.. autofunction:: fetch_adk_transitions_DIMS



.. include:: ../MDAnalysisData/descr/adk_transitions_FRODA.rst

.. autofunction:: fetch_adk_transitions_FRODA
		  
		  

		  
.. rubric:: References

.. [Perilla2009] J. R. Perilla, O. Beckstein, E. J. Denning,
    and T. Woolf. Computing ensembles of transitions from stable
    states: Dynamic importance sampling. 32(2):186–209, 2011.

.. [Farrell2010] D. W. Farrell, K. Speranskiy,
    and M. F. Thorpe. Generating stereochemically acceptable protein
    pathways. Proteins, 78(14):2908–21, Nov 2010.

.. [Seyler2014] S. L. Seyler and O. Beckstein. Sampling of large
   conformational transitions: Adenylate kinase as a testing
   ground. Molec. Simul., 40(10–11):855–877, 2014.
		
.. [Seyler2015] Seyler SL, Kumar A, Thorpe MF, Beckstein O (2015) Path
   Similarity Analysis: A Method for Quantifying Macromolecular
   Pathways. PLoS Comput Biol 11(10): e1004568. doi:
   `10.1371/journal.pcbi.1004568
   <https://doi.org/10.1371/journal.pcbi.1004568>`_
	    
