# MDAnalysisData package
#
# Modelled after sklearn.datasets
# https://github.com/scikit-learn/scikit-learn/tree/0.20.X/sklearn/datasets

__all__ = ['datasets']

from . import datasets

from . import _version
__version__ = _version.get_versions()['version']

try:
    from .authors import __authors__
except ImportError:
    import warnings
    warnings.warn('Could not find authors.py, __authors__ will be the '
                  'generic MDAnalysis team.')
    __authors__ = ["The MDAnalysis Development Team"]
    del warnings
