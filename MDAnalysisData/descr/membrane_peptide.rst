.. -*- coding: utf-8 -*-

.. _`membrane-peptide-dataset`:


Peptide in DMPC membrane dataset
================================

Molecular dynamics simulation of a 19-residue peptide inside a pure
DMPC membrane with water at full atomic detail with explicit
solvent. The total simulated time is 1 ns.

The simulation was performed in the NPT ensemble at 1 atm at 310K
using Berendsen (semi-isotropic) and V-rescale for pressure and
temperature coupling, respectively, with 1.6 ps and 0.1 ps as coupling
constants. Van der Waals interactions were treated using the Verlet
algorithm with a 1 nm cutoff. Electrostatics where treated with
particle-mesh Ewald, with a 1 nm cutoff for the real space
calculations. Both the peptide and DMPC were parameterized using the
GROMOS 54A7 force field, while the SPC model was used for water. LINCS
restraints were used on all the bonds.

The peptide sequence is ``AAAQAAQAQWAQRQATWQA``. This sequence was not
taken from any real world examples, as this is a test system created
for MDAnalysis datasets. The peptide was set to have a α-helical
secondary structure, and was inserted manually in the membrane before
minimization and equilibration.

The topology is contained in the TPR file (Gromacs format). The
trajectory is contained in the XTC file (Gromacs compressed
coordinates format).

Notes
-----

Data set characteristics:

 :size: 67 MB
 :number of trajectories: 1
 :number of frames:  1001
 :number of particles: 18727
 :creator: Davide Cruz
 :URL:  `10.6084/m9.figshare.8046437.v1 <https://doi.org/10.6084/m9.figshare.8046437.v1>`_
 :license: `CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/legalcode>`_
