# -*- coding: utf-8 -*-

"""Ensembles of AdK transitions.

https://figshare.com/articles/Simulated_trajectory_ensembles_for_the_closed-to-open_transition_of_adenylate_kinase_from_DIMS_MD_and_FRODA/7165306
"""


from os.path import dirname, exists, join
from os import makedirs, remove
import tarfile
import glob

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch


METADATA = {
    'DIMS': {
        'NAME': "adk_transitions_DIMS",
        'DESCRIPTION': "adk_transitions_DIMS.rst",
        'ARCHIVE': {
            'tarfile': RemoteFileMetadata(
                filename='DIMS.tar.gz',
                url='https://ndownloader.figshare.com/files/13182490',
                checksum='81dfd247da7084bc7f47889c098069978b61f8f8b4f7706841266d284bfd3b55',
            ),
        },
        'CONTENTS': {
            'topology': "DIMS/topologies/adk4ake.psf",
            'trajectories': "DIMS/trajectories/dims*_fit-core.dcd",
            'N_trajectories': 200,
        },
    },
    'FRODA': {
        'NAME': "adk_transitions_FRODA",
        'DESCRIPTION': "adk_transitions_FRODA.rst",
        'ARCHIVE': {
            'tarfile': RemoteFileMetadata(
                filename='FRODA.tar.gz',
                url='https://ndownloader.figshare.com/files/13182493',
                checksum='fc2c90b9819fd07720e7effada033d4045663919ba7d2c8bd84f548dfbeee73c',
            ),
        },
        'CONTENTS': {
            'topology': "FRODA/topologies/1ake.pdb",
            'trajectories': "FRODA/trajectories/pathway*_fit-core.dcd",
            'N_trajectories': 200,
        },
    },
}

logger = logging.getLogger(__name__)

def fetch_adk_transitions_DIMS(data_home=None, download_if_missing=True):
    """Load the AdK DIMS transititions dataset

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/adk_transitions_DIMS``.
    download_if_missing : optional, default=True
        If ``False``, raise a :exc:`IOError` if the data is not locally available
        instead of trying to download the data from the source site.

    Returns
    -------
    dataset : dict-like object with the following attributes:
    dataset.topology : filename
        Filename of the topology file
    dataset.trajectories : list
        list with filenames of the trajectory ensemble
    dataset.N_trajectories : int
        number of trajectories in the ensemble
    dataset.DESCR : string
        Description of the ensemble


    See :ref:`adk-transitions-DIMS-dataset` for description.
    """
    return _fetch_adk_transitions(METADATA['DIMS'],
                                  data_home=data_home,
                                  download_if_missing=download_if_missing)

def fetch_adk_transitions_FRODA(data_home=None, download_if_missing=True):
    """Load the AdK FRODA transititions dataset

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/adk_transitions_FRODA``.
    download_if_missing : optional, default=True
        If ``False``, raise a :exc:`IOError` if the data is not locally available
        instead of trying to download the data from the source site.

    Returns
    -------
    dataset : dict-like object with the following attributes:
    dataset.topology : filename
        Filename of the topology file
    dataset.trajectories : list
        list with filenames of the trajectory ensemble
    dataset.N_trajectories : int
        number of trajectories in the ensemble
    dataset.DESCR : string
        Description of the ensemble


    See :ref:`adk-transitions-FRODA-dataset` for description.
    """
    return _fetch_adk_transitions(METADATA['FRODA'],
                                  data_home=data_home,
                                  download_if_missing=download_if_missing)


def _fetch_adk_transitions(metadata, data_home=None, download_if_missing=True):
    """Generic function to load the AdK transititions datasets

    Parameters
    ----------
    metdata : dict
        dictionary with `NAME`, `DESCRIPTION` and `ARCHIVE` that contains
        a tar.gz file with directories topologies and trajectories
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
    download_if_missing : optional, default=True
        If ``False``, raise a :exc:`IOError` if the data is not locally available
        instead of trying to download the data from the source site.

    Returns
    -------
    dataset : dict-like object with the following attributes:
    dataset.topology : filename
        Filename of the topology file
    dataset.trajectories : list
        list with filenames of the trajectory ensemble
    dataset.DESCR : string
        Description of the ensemble

    Note
    ----
    Assumptions that are built in:
    - download a single tar.gz file
    - trajectories are given with a glob pattern

    """
    name = metadata['NAME']
    data_location = join(get_data_home(data_home=data_home),
                         name)
    if not exists(data_location):
        makedirs(data_location)

    records = Bunch()

    meta = metadata['ARCHIVE']['tarfile']
    local_path = join(data_location, meta.filename)

    if not exists(local_path):
        if not download_if_missing:
            raise IOError("Data {0}={1} not found and `download_if_missing` is "
                          "False".format(file_type, local_path))
        logger.info("Downloading {0}: {1} -> {2}...".format(
            "tarfile", meta.url, local_path))
        archive_path = _fetch_remote(meta, dirname=data_location)

        logger.info("Unpacking {}...".format(archive_path))
        with tarfile.open(archive_path, 'r') as tar:
            tar.extractall(path=data_location)

    records.topology = join(data_location, metadata['CONTENTS']['topology'])
    if not exists(records.topology):
        # should not happen...
        raise RuntimeError("topology file {} is missing".format(records.topology))

    trajectory_pattern = join(data_location, metadata['CONTENTS']['trajectories'])
    records.trajectories = glob.glob(trajectory_pattern)
    records.N_trajectories = metadata['CONTENTS']['N_trajectories']
    if len(records.trajectories) != records.N_trajectories:
        # should not happen...
        raise RuntimeError("trajectory files in {0} are incomplete: only {1} "
                           "but should be {2}.".format(
                               trajectory_pattern, len(records.trajectories),
                               records.N_trajectories))

    records.DESCR = _read_description(metadata['DESCRIPTION'])

    return records
