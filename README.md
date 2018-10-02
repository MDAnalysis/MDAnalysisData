# MDAnalysisData
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


## Accessing data sets 

Import the datasets and access your data set of choice:
```python
from MDAnalysisData import datasets

adk = datasets.fetch_adk()
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
MDANALYSIS_DATA=/tmp/MDAnalysis_data
```

The location of the data directory can be obtained with
```python
MDAnalysisData.base.get_data_home()
```

If the data directory is removed then data are downloaded again. Data
file integrity is checked with a SHA256 checksum when the file is
downloaded (but not at later).

The data directory can we wiped with the function
```python
MDAnalysisData.base.clear_data_home()
```



## Credits

This package is modelled after
[sklearn.datasets](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets). It
uses code from `sklearn.datasets` (under the [BSD 3-clause
license](https://github.com/scikit-learn/scikit-learn/blob/master/COPYING)).

No data is included; please see the `DESCR` attribute for each data
set for authorship, citation, and license information for the data.


