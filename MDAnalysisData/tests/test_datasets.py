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
import glob

import pytest

from MDAnalysisData import base
from MDAnalysisData import datasets
from MDAnalysisData import adk_equilibrium
from MDAnalysisData import ifabp_water
from MDAnalysisData import nhaa_equilibrium
from MDAnalysisData import CG_fiber
from MDAnalysisData import vesicles
from MDAnalysisData import adk_transitions
from MDAnalysisData import membrane_peptide
from MDAnalysisData import yiip_equilibrium

# For filetype=topology, the data are downloaded and cached.
# For filetype=trajectory the cached data are used.
# This test is not thread/parallel safe.

@pytest.mark.online
@pytest.mark.parametrize('filetype', ('topology', 'trajectory'))
def test_adk_equilibrium(filetype):
    data = datasets.fetch_adk_equilibrium()

    metadata = adk_equilibrium.ARCHIVE

    assert len(data.DESCR) == 1252
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`adk-equilibrium-dataset`:")

    assert os.path.basename(data[filetype]) == metadata[filetype].filename
    assert os.path.exists(data[filetype])

@pytest.mark.online
@pytest.mark.parametrize('filetype', ('topology',
                                      'trajectory',
                                      'structure'))
def test_ifabp_water(filetype):
    data = datasets.fetch_ifabp_water()

    metadata = ifabp_water.ARCHIVE

    assert len(data.DESCR) == 1098
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`ifabp-water-dataset`:")

    assert os.path.basename(data[filetype]) == metadata[filetype].filename
    assert os.path.exists(data[filetype])


@pytest.mark.online
@pytest.mark.parametrize('filetype', ('topology', 'trajectory'))
def test_nhaa_equilibrium(filetype):
    data = datasets.fetch_nhaa_equilibrium()

    metadata = nhaa_equilibrium.ARCHIVE

    assert len(data.DESCR) == 1475
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`nhaa-equilibrium-dataset`:")

    assert os.path.basename(data[filetype]) == metadata[filetype].filename
    assert os.path.exists(data[filetype])


@pytest.mark.online
@pytest.mark.parametrize('filetype', ('topology', 'trajectory'))
def test_CG_fiber(filetype):
    data = datasets.fetch_CG_fiber()

    metadata = CG_fiber.ARCHIVE

    assert len(data.DESCR) == 535
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`CG_fiber-dataset`:")

    assert os.path.basename(data[filetype]) == metadata[filetype].filename
    assert os.path.exists(data[filetype])


@pytest.mark.online
@pytest.mark.parametrize('filename',
                         vesicles.METADATA['vesicle_lib']['CONTENTS']['structures'])
def test_vesicles(filename):
    data = datasets.fetch_vesicle_lib()

    metadata = vesicles.METADATA['vesicle_lib']

    assert len(data.DESCR) == 1329
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`vesicle-library-dataset`:")

    assert data.N_structures == metadata['CONTENTS']['N_structures']
    assert data.N_structures == len(metadata['CONTENTS']['structures'])
    assert any(path.endswith(filename) for path in data.structures)
    assert any(os.path.exists(path) for path in data.structures if path.endswith(filename))


@pytest.mark.online
@pytest.mark.parametrize('method,descr_length',
                         (('DIMS', 1395),
                          ('FRODA', 1399)))
@pytest.mark.parametrize('filetype', ('topology', 'trajectories'))
def test_adk_transitions(method, descr_length, filetype):
    if method == "DIMS":
        data = datasets.fetch_adk_transitions_DIMS()
    elif method == "FRODA":
        data = datasets.fetch_adk_transitions_FRODA()
    else:
        raise ValueError("Unknown adk_transitions method '{}'".format(method))

    metadata = adk_transitions.METADATA[method]['CONTENTS']

    assert len(data.DESCR) == descr_length
    descr_header = (".. -*- coding: utf-8 -*-\n\n"
                    ".. _`adk-transitions-{}-dataset`:".format(
                        method))
    assert data.DESCR.startswith(descr_header)

    datafiles = data[filetype] if isinstance(data[filetype], list) \
        else [data[filetype]]
    pattern = os.path.join("*", metadata[filetype])

    assert all(glob.fnmatch.fnmatch(path, pattern) for path in datafiles), \
        "not all datafiles {} match {}".format(datafiles, pattern)
    assert all(os.path.exists(path) for path in datafiles)


@pytest.mark.online
@pytest.mark.parametrize('filetype', ('topology', 'trajectory'))
def test_membrane_peptide(filetype):
    data = datasets.fetch_membrane_peptide()

    metadata = membrane_peptide.ARCHIVE

    assert len(data.DESCR) == 1657
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`membrane-peptide-dataset`:")

    assert os.path.basename(data[filetype]) == metadata[filetype].filename
    assert os.path.exists(data[filetype])


@pytest.mark.online
@pytest.mark.parametrize('traj_len', ('short', 'long'))
@pytest.mark.parametrize('filetype', ('topology', 'trajectory'))
def test_yiip_equilibrium(traj_len, filetype):
    if traj_len == "short":
        data = datasets.fetch_yiip_equilibrium_short()
    elif traj_len == "long":
        data = datasets.fetch_yiip_equilibrium_long()
    else:
        raise ValueError("Unknown yiip_equilibrium trajectory length'{}'".format(traj_len))

    metadata = yiip_equilibrium.ARCHIVE[traj_len]

    assert len(data.DESCR) == 1511
    assert data.DESCR.startswith(".. -*- coding: utf-8 -*-\n\n.. _`yiip-equilibrium-dataset`:")

    assert os.path.basename(data[filetype]) == metadata[filetype].filename
    assert os.path.exists(data[filetype])

