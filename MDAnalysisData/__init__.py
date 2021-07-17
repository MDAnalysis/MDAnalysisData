# MDAnalysisData package
#
# Modelled after sklearn.datasets
# https://github.com/scikit-learn/scikit-learn/tree/0.20.X/sklearn/datasets

from __future__ import absolute_import

__all__ = ['datasets']

from . import datasets

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

try:
    from .authors import __authors__
except ImportError:
    import warnings
    warnings.warn('Could not find authors.py, __authors__ will be the '
                  'generic MDAnalysis team.')
    __authors__ = ["The MDAnalysis Development Team"]
    del warnings
