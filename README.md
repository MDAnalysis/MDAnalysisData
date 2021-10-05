# MDAnalysisData

[![Build Status](https://github.com/MDAnalysis/MDAnalysisData/actions/workflows/gh-ci.yml/badge.svg)](https://github.com/MDAnalysis/MDAnalysisData/actions/workflows/gh-ci.yml)
[![codecov](https://codecov.io/gh/MDAnalysis/MDAnalysisData/branch/master/graph/badge.svg)](https://codecov.io/gh/MDAnalysis/MDAnalysisData)
[![docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://www.mdanalysis.org/MDAnalysisData/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/mdanalysisdata/badges/version.svg)](https://anaconda.org/conda-forge/mdanalysisdata)
[![DOI](https://zenodo.org/badge/147885122.svg)](https://zenodo.org/badge/latestdoi/147885122)

Access to data for workshops and extended tests of MDAnalysis.

Data sets are stored at external stable URLs (e.g., on
[figshare](https://figshare.com/), [zenodo](https://zenodo.org/), or
[DataDryad](https://www.datadryad.org/)) and this package provides a
simple interface to download, cache, and access data sets.

## Installation

To use, install the package
```bash
pip install --upgrade MDAnalysisData
```

or install with `conda`
```bash
conda install --channel conda-forge mdanalysisdata
```

## Accessing data sets 

Import the datasets and access your data set of choice:
```python
from MDAnalysisData import datasets

adk = datasets.fetch_adk_equilibrium()
```


The returned object contains attributes with the paths to topology and
trajectory files so that you can use it directly with, for instance, [MDAnalysis](https://www.mdanalysis.org):
```python
import MDAnalysis as mda
u = mda.Universe(adk.topology, adk.trajectory)
```

The metadata object also contains a `DESCR` attribute with a
description of the data set, including relevant citations:
```python
print(adk.DESCR)
```

## Managing data

Data are locally stored in the **data directory** `~/MDAnalysis_data`
(i.e., in the user's home directory). This location can be changed by
setting the environment variable `MDANALYSIS_DATA`, for instance
```bash
export MDANALYSIS_DATA=/tmp/MDAnalysis_data
```

The location of the data directory can be obtained with
```python
MDAnalysisData.base.get_data_home()
```

If the data directory is removed then data are downloaded again. Data
file integrity is checked with a SHA256 checksum when the file is
downloaded.

The data directory can we wiped with the function
```python
MDAnalysisData.base.clear_data_home()
```

## Contributing new datasets

Please add new datasets to MDAnalysisData. See [Contributing new
datasets](https://www.mdanalysis.org/MDAnalysisData/contributing.html)
for details, but in short:

1. raise an issue in the [issue
   tracker](https://github.com/MDAnalysis/MDAnalysisData/issues) describing
   what you want to add; this issue will become the focal point for discussions
   where the developers can easily give advice
2. deposit data in an archive under an [Open
   Data](https://opendatacommons.org/) compatible license (CC0 or
   CC-BY preferred)
3. write accessor code in MDAnalysisData


## Credits

This package is modelled after
[sklearn.datasets](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets). It
uses code from `sklearn.datasets` (under the [BSD 3-clause
license](https://github.com/scikit-learn/scikit-learn/blob/master/COPYING)).

No data are included; please see the `DESCR` attribute for each data
set for authorship, citation, and license information for the data.


