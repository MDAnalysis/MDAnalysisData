# MDAnalysisData package
#
# Modelled after sklearn.datasets
# https://github.com/scikit-learn/scikit-learn/tree/0.20.X/sklearn/datasets

__all__ = ['datasets']

from . import datasets


from importlib.metadata import version
__version__ = version("MDAnalysisData")
