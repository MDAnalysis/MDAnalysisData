# -*- coding: utf-8 -*-

import sys
from importlib import reload
import pytest

import MDAnalysisData


def test_version():
    # very generic because versioneer will provide different strings depending
    # on the repository status
    assert isinstance(MDAnalysisData.__version__, str)
