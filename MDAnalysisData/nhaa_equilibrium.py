# -*- coding: utf-8 -*-

"""NhaA equilibrium trajectory without water.

https://figshare.com/articles/Molecular_dynamics_trajectory_of_membrane_protein_NhaA/7185203/2
"""

from os.path import dirname, exists, join
from os import makedirs, remove
import codecs

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "nhaa_equilibrium"
DESCRIPTION = "nhaa_equilibrium.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'topology': RemoteFileMetadata(
        filename='NhaA_non_water.gro',
        url='https://ndownloader.figshare.com/files/13222709',
        checksum='ae42f4cfcfe312476f9e5121fe47764a11aff962197799671c0c5a8f83637420',
    ),
    'trajectory':  RemoteFileMetadata(
        filename='NhaA_non_water.xtc',
        url='https://ndownloader.figshare.com/files/13222712',
        checksum='c9ab7ba8c9c271d535cfadebc33da1d90fbf00d9a01f48afedd0f7a703128eaf',
    ),
}

logger = logging.getLogger(__name__)


def fetch_nhaa_equilibrium(data_home=None, download_if_missing=True):
    """Load the NhaA 500 ns equilibrium trajectory (without water)

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/nhaa_equilibrium``.
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


    See :ref:`nhaa-equilibrium-dataset` for description.
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
