# -*- coding: utf-8 -*-

import sys
from importlib import reload
import pytest

import MDAnalysisData


def test_authors():
    authors = MDAnalysisData.__authors__
    assert authors[:6] == ["Irfan Alibay", "Oliver Beckstein", "Shujie Fan",
                           "Richard J. Gowers", "Micaela Matta",
                           "Lily Wang"]


def test_default_authors(monkeypatch):
    # authors.py did not exist and could not be imported
    monkeypatch.setitem(sys.modules, 'MDAnalysisData.authors', None)
    with pytest.warns(UserWarning,
                      match="Could not find authors.py, __authors__ will "
                            "be the generic MDAnalysis team."):
        reload(MDAnalysisData)
    authors = MDAnalysisData.__authors__
    assert authors == ["The MDAnalysis Development Team"]


def test_version():
    # very generic because versioneer will provide different strings depending
    # on the repository status
    assert isinstance(MDAnalysisData.__version__, str)
