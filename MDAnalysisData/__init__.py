# MDAnalysisData package
#
# Modelled after sklearn.datasets
# https://github.com/scikit-learn/scikit-learn/tree/0.20.X/sklearn/datasets

from __future__ import absolute_import

__all__ = ['datasets']

from . import datasets
from .base import fetch, DATASET_NAMES




from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
