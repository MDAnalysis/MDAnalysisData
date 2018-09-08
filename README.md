# MDAnalysisData
Access to data for workshops and extended tests of MDAnalysis.

Data sets are stored at external stable URLs (e.g., on
[figshare](https://figshare.com/), [zenodo](https://zenodo.org/), or
[DataDryad](https://www.datadryad.org/)) and this package provides a
simple interface to download, cache, and access data sets.

To use, install the package
```bash
pip install --upgrade MDAnalysisData
```
and import it and access your data set of choice:
```python
from MDAnalysisData import datasets

adk = datasets.fetch_adk()
```

This package is modelled after [sklearn.datasets](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets).



