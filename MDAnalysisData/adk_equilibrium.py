# -*- coding: utf-8 -*-

"""AdK equilibrium trajectory without water.

https://figshare.com/articles/Molecular_dynamics_trajectory_for_benchmarking_MDAnalysis/5108170/1
"""

from os.path import dirname, exists, join
from os import makedirs, remove

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "adk_equilibrium"
DESCRIPTION = "adk_equilibrium.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'topology': RemoteFileMetadata(
        filename='adk4AKE.psf',
        url='https://ndownloader.figshare.com/files/8672230',
        checksum='1aa947d58fb41b6805dc1e7be4dbe65c6a8f4690f0bd7fc2ae03e7bd437085f4',
    ),
    'trajectory':  RemoteFileMetadata(
        filename='1ake_007-nowater-core-dt240ps.dcd',
        url='https://ndownloader.figshare.com/files/8672074',
        checksum='598fcbcfcc425f6eafbe9997238320fcacc6a4613ecce061e1521732bab734bf',
    ),
}

logger = logging.getLogger(__name__)


def fetch_adk_equilibrium(data_home=None, download_if_missing=True):
    """Load the AdK 1us equilibrium trajectory (without water)

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/adk_equilibrium``.
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


    See :ref:`adk-equilibrium-dataset` for description.
    """
    name = NAME
    data_location = join(get_data_home(data_home=data_home),
                         name)
    if not exists(data_location):
        makedirs(data_location)

    records = Bunch()
    for file_type, meta in ARCHIVE.items():
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
