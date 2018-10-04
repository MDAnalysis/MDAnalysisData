# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- streamlined the typical `fetch_NAME()` function by using module
  level variables
  
### Added
- new `fetch_ifabp_water()` to get the IFABP+water data set from
  https://figshare.com/articles/Molecular_dynamics_trajectory_of_I-FABP_for_testing_and_benchmarking_solvent_dynamics_analysis/7058030
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
