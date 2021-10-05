# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.1] - 2021-10-04

### Added
- docs for how to contribute a new dataset (#46)
- new `MDAnalysis.__authors__` attribute with the list of AUTHORS

### Changes
- update online docs theme (#43)
- tested for Python 2.7, 3.6 - 3.9 on Linux, macOS, Windows (#48)

## [0.8.0] - 2019-08-13

### Added
- YiiP equilibrium dataset used for benchmarks in the PMDA paper:
  `fetch_yiip_equilibrium_short` to get a 9-ns YiiP trajectory and
  `fetch_yiip_equilibrium_long` to get a 90-ns YiiP trajectory (#39)

## [0.7.0] - 2019-04-26

### Added
- `fetch_membrane_peptide()` to get a membrane peptide dataset (#34)

### Fixes
- doc fixes (PEG 1 chain dataset)

### Fixes (internal)
- CI: pip upgrade all dependencies (#36)


## [0.6.0] - 2018-11-11

### Added
- PEG_1chain dataset


## [0.5.0] - 2018-11-06
### Fixes
- vesicles dataset: failed to get description

### Added
- progressbar for downloads (#29)

### Changes (internal)
- tests with full downloads can be performed with
  `pytest -m online`; by default `pytest -m 'not online'` is run,
  which skips downloading gigabytes of data (PR #18)


## [0.4.0] - 2018-10-05
### Added
- new `fetch_CG_fiber()` to get CG_fiber dataset (PR #24)

### Fixes
- fixed fetch_adk_transitions_DIMS() failed to fetch (#19)
- added six to install requirements (#22)
- added setuptools to install requirements (#23)


## [0.3.0] - 2018-10-11
### Fixes
- fixed description of 'AdK equilibrium' dataset
- fixed loading descriptions from zipped eggs (#12)

### Added
- new `fetch_nhaa_equilibrium()` to get the NhaA trajectory from
  https://figshare.com/articles/Molecular_dynamics_trajectory_of_membrane_protein_NhaA/7185203/2
  (see issue #7)
- new internal function `base._read_description()` to simplify reading of the
  descr.rst files into datasets
- continuous integration/tests: MDAnalysisData should be compatible with Python
  2.7 and Python 3.4+. It is currently tested on 2.7 and 3.6.

### Changes
- Default location of the data_home is now stored as `base.DEFAULT_DATADIR`.


## [0.2.2] - 2018-10-05
### Fixes
- all dataset descriptions now contain *number of trajectories*
  information

### Changes
- changed the labels in the vesicles dataset to match documentation

## [0.2.1] - 2018-10-05
### Added
- documentation (#4)
- automatic deployment of docs to
  https://www.mdanalysis.org/MDAnalysisData/ via Travis-CI (#4)


## [0.2.0] - 2018-10-04
### Changed
- streamlined the typical `fetch_NAME()` function by using module
  level variables  
- added *size* information (unpacked data in MB) to the canonical descriptions

### Added
- new `fetch_ifabp_water()` to get the IFABP+water data set from
  https://figshare.com/articles/Molecular_dynamics_trajectory_of_I-FABP_for_testing_and_benchmarking_solvent_dynamics_analysis/7058030
  (see issue #5)
- new `fetch_adk_transitions_DIMS()` and
  `fetch_adk_transitions_FRODA()` functions to get the trajectory
  ensembles from
  https://figshare.com/articles/Simulated_trajectory_ensembles_for_the_closed-to-open_transition_of_adenylate_kinase_from_DIMS_MD_and_FRODA/7165306
  (see issue #5)
- new `fetch_vesicle_lib()` function to get the structures from
  https://figshare.com/articles/Large_System_Vesicle_Benchmark_Library/3406708
  (see issue #5)


## [0.1.1] - 2018-10-02
### Fixed
- documentation in README fixed

## [0.1.0] - 2018-10-02
initial public release

### Added
- basic functionality (based on sklearn.datasets)
- AdK equilibrium data set from
  https://figshare.com/articles/Molecular_dynamics_trajectory_for_benchmarking_MDAnalysis/5108170
  (issue #1)
