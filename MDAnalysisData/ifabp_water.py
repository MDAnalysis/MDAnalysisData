# -*- coding: utf-8 -*-

"""MD simulation of I-FABP with water.

https://figshare.com/articles/Molecular_dynamics_trajectory_of_I-FABP_for_testing_and_benchmarking_solvent_dynamics_analysis/7058030
"""

from os.path import dirname, exists, join
from os import makedirs, remove

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "ifabp_water"
DESCRIPTION = "ifabp_water.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'topology': RemoteFileMetadata(
        filename='ifabp_water.psf',
        url='https://ndownloader.figshare.com/files/12980639',
        checksum='ba40714318aabec537015dc550fe5bd5ac1ac0b853f5abdd2f0ae63af9cfcafa',
    ),
    'structure': RemoteFileMetadata(
        filename='ifabp_water_0.pdb',
        url='https://ndownloader.figshare.com/files/12980636',
        checksum='8ccf5f75fd85385921c0cb77f00281a93b933fc1261c42fc9492f43983448a72',
    ),
    'trajectory':  RemoteFileMetadata(
        filename='rmsfit_ifabp_water_1.dcd',
        url='https://ndownloader.figshare.com/files/12980642',
        checksum='cebb48e58015abc8ff2f5bb7ba3eb7a289047f256351a8252bf1f29f9aaacf0e',
    ),
}



logger = logging.getLogger(__name__)


def fetch_ifabp_water(data_home=None, download_if_missing=True):
    """Load the I-FABP with water 0.5 ns equilibrium trajectory

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/ifabp_water``.
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
    dataset.structure : filename
        Filename of a structure file in PDB format
    dataset.DESCR : string
        Description of the trajectory.


    See :ref:`ifabp-water-dataset` for description.
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
