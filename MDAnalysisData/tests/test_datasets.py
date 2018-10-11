# -*- coding: utf-8 -*-

# Downloading all datasets takes a long time. We do not want to do this
# for the normal tests.
#
# We could cache the data_home directory on Travis CI
# https://docs.travis-ci.com/user/caching/ although the docs say "Large files
# that are quick to install but slow to download do not benefit from caching,
# as they take as long to download from the cache as from the original source."

from __future__ import absolute_import, division

import os.path

import pytest

from MDAnalysisData import base
from MDAnalysisData import datasets
from MDAnalysisData import adk_equilibrium


# For filetype=topology, the data are downloaded and cached.
# For filetype=trajectory the cached data are used.
# This test is not thread/parallel safe.

@pytest.mark.parametrize('filetype', ('topology', 'trajectory'))
def test_adk_equilibrium(filetype):
    adk = datasets.fetch_adk_equilibrium()

    metadata = adk_equilibrium.ARCHIVE

    assert len(adk.DESCR) == 1252
    assert adk.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`adk-equilibrium-dataset`:")

    assert os.path.basename(adk[filetype]) == metadata[filetype].filename
    assert os.path.exists(adk[filetype])
