.. -*- coding: utf-8 -*-

.. _`nhaa-equilibrium-dataset`:

NhaA equilibrium trajectory dataset
===================================

Molecular dynamics (MD) trajectory of the NhaA membrane protein in a
POPE:POPG 4:1 model membrane. The equilibrium simulation was performed
in the NPT ensemble at T=300K and P=1 bar. The system was simulated
with Gromacs 5.1.4, using the CHARMM36 force field, the TIP3P explicit
water model, and NaCl at approximately 100 mM concentration. 

Trajectory frames were saved every 100 ps for a total of 500 ns
simulated time. The topology only contains the protein, membrane and
ions (because the water molecules were stripped from the trajectory to
save space).

The topology is contained in the NhaA_non_water.gro file. The trajectory is contained in the NhaA_non_water.xtc file.


Notes
-----

Data set characteristics:

 :size: 1.07 GB
 :number of trajectories: 1
 :number of frames:  5000
 :number of particles: 60702
 :creator: Ian Kenney, Shujie Fan
 :URL:  `10.6084/m9.figshare.7185203.v2 <https://doi.org/10.6084/m9.figshare.7185203.v2>`_
 :license: `CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/legalcode>`_
 :reference: [Kenney2018]_


.. [Kenney2018]  M. Kenney, Ian; Fan, Shujie; Beckstein, Oliver (2018): Molecular dynamics
           trajectory of membrane protein NhaA. figshare. Dataset.
	   MDAnalysis. figshare. Fileset. doi:
	   `10.6084/m9.figshare.7185203.v2
	   <https://doi.org/10.6084/m9.figshare.7185203.v2>`_

