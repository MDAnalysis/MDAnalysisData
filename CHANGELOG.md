# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
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
