"""YiiP equilibrium trajectory with water.

https://figshare.com/articles/Molecular_Dynamics_trajectories_of_membrane_protein_YiiP/8202149
"""

from os.path import dirname, exists, join
from os import makedirs, remove
import codecs

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "yiip_equilibrium"
DESCRIPTION = "yiip_equilibrium.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'short':{
        'topology': RemoteFileMetadata(
            filename='YiiP_system.pdb',
            url='https://ndownloader.figshare.com/files/15286808',
            checksum='3c2b96bbd2f95105e1a4f37140132ee073a947df8fe209a8170f09ca5b73e6cf',
            ),
        'trajectory':  RemoteFileMetadata(
            filename='YiiP_system_9ns_center.xtc',
            url='https://ndownloader.figshare.com/files/15285461',
            checksum='97f6a93acc1e330915338b290625d81d84928a7e4c1e5aed63d209881fbe268b',
            ),
    },
    'long':{
        'topology': RemoteFileMetadata(
            filename='YiiP_system.pdb',
            url='https://ndownloader.figshare.com/files/15286808',
            checksum='3c2b96bbd2f95105e1a4f37140132ee073a947df8fe209a8170f09ca5b73e6cf',
            ),
        'trajectory':  RemoteFileMetadata(
            filename='YiiP_system_90ns_center.xtc',
            url='https://ndownloader.figshare.com/files/15294914',
            checksum='de16552ad0eb46144a7fe980424b4f3b89bf6ae553512a246d5015e5a361033c',
            ),
    },
}

logger = logging.getLogger(__name__)


def fetch_yiip_equilibrium_short(data_home=None, download_if_missing=True):
    """Load the YiiP 9 ns equilibrium trajectory

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/yiip_equilibrium``.
    download_if_missing : optional, default=True
        If ``False``, raise a :exc:`IOError` if the data is not locally available
        instead of trying to download the data from the source site.

    Returns
    -------
    dataset : dict-like object with the following attributes:
    dataset.topology : filename
        Filename of the topology file
    dataset.trajectory : filename
        Filename of the trajectory file
    dataset.DESCR : string
        Description of the trajectory.


    See :ref:`yiip-equilibrium-dataset` for description.
    """
    name = NAME
    data_location = join(get_data_home(data_home=data_home),
                         name)
    if not exists(data_location):
        makedirs(data_location)

    records = Bunch()
    for file_type, meta in ARCHIVE['short'].items():
        local_path = join(data_location, meta.filename)
        records[file_type] = local_path

        if not exists(local_path):
            if not download_if_missing:
                raise IOError("Data {0}={1} not found and `download_if_missing` is "
                              "False".format(file_type, local_path))
            logger.info("Downloading {0}: {1} -> {2}...".format(
                file_type, meta.url, local_path))
            archive_path = _fetch_remote(meta, dirname=data_location)

    records.DESCR = _read_description(DESCRIPTION)

    return records


def fetch_yiip_equilibrium_long(data_home=None, download_if_missing=True):
    """Load the YiiP 90 ns equilibrium trajectory

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/yiip_equilibrium``.
    download_if_missing : optional, default=True
        If ``False``, raise a :exc:`IOError` if the data is not locally available
        instead of trying to download the data from the source site.

    Returns
    -------
    dataset : dict-like object with the following attributes:
    dataset.topology : filename
        Filename of the topology file
    dataset.trajectory : filename
        Filename of the trajectory file
    dataset.DESCR : string
        Description of the trajectory.


    See :ref:`yiip-equilibrium-dataset` for description.
    """
    name = NAME
    data_location = join(get_data_home(data_home=data_home),
                         name)
    if not exists(data_location):
        makedirs(data_location)

    records = Bunch()
    for file_type, meta in ARCHIVE['long'].items():
        local_path = join(data_location, meta.filename)
        records[file_type] = local_path

        if not exists(local_path):
            if not download_if_missing:
                raise IOError("Data {0}={1} not found and `download_if_missing` is "
                              "False".format(file_type, local_path))
            logger.info("Downloading {0}: {1} -> {2}...".format(
                file_type, meta.url, local_path))
            archive_path = _fetch_remote(meta, dirname=data_location)

    records.DESCR = _read_description(DESCRIPTION)

    return records
