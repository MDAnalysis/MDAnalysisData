.. -*- coding: utf-8 -*-

.. _`yiip-equilibrium-dataset`:

YiiP equilibrium trajectory dataset
===================================

Molecular dynamics (MD) trajectory files of the YiiP membrane protein in
a POPE:POPG 4:1 model membrane. The equilibrium simulation was performed
in the NPT ensemble at T=300K and P=1 bar. The system was simulated with
Gromacs 2018.1, using the CHARMM36 force field, the TIP3P explicit water
model, NaCl at approximately 100 mM concentration, and Zinc ions.

Trajectory frames were saved every 100 ps for a total of 9 ns and 90 ns
simulated time. The topology contains the whole system (protein, membrane,
water and ions).

The topology is contained in the YiiP_system.pdb file. The 9-ns trajectory
is contained in the ``YiiP_system_9ns_center.xtc`` file. The 90-ns trajectory
is contained in the ``YiiP_system_90ns_center.xtc`` file.


Notes
-----

Data set characteristics:

 :size: 3.82 GB
 :number of trajectories: 2
 :number of frames:  900 (short), 9000 (long)
 :number of particles: 111815
 :creator: Shujie Fan, Oliver Beckstein
 :URL:  `10.6084/m9.figshare.8202149.v1 <https://doi.org/10.6084/m9.figshare.8202149.v1>`_
 :license: `CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/legalcode>`_
 :reference: [Fan2019]_


.. [Fan2019]  Fan, Shujie; Beckstein, Oliver (2019): Molecular dynamics
           trajectory of membrane protein YiiP. figshare. Dataset.
	   MDAnalysis. figshare. Fileset. doi:
	   `10.6084/m9.figshare.8202149.v1
	   <https://doi.org/10.6084/m9.figshare.8202149.v1>`_
