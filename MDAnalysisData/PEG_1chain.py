# -*- coding: utf-8 -*-

"""Molecular dynamics trajectory of a single PEG chain in TIP3P water.

https://doi.org/10.6084/m9.figshare.7325774
"""

from os.path import dirname, exists, join
from os import makedirs, remove

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "PEG_1chain"
DESCRIPTION = "PEG_1chain.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'topology': RemoteFileMetadata(
        filename='PEG.prmtop',
        url='https://ndownloader.figshare.com/files/13532462',
        checksum='2d7955b9a8cb6e008171e0c5a1c31e3e458246ea3ee7302281eafefafa7cede9',
    ),
    'trajectory':  RemoteFileMetadata(
        filename='PEG_03_prod.nc',
        url='https://ndownloader.figshare.com/files/13532465',
        checksum='b978714ec2f93d1cbe99564cb257959f0cb38872359aa745c8eba720a7d85225',
    ),
}

logger = logging.getLogger(__name__)


def fetch_PEG_1chain(data_home=None, download_if_missing=True):
    """Load the PEG polymer trajectory

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/CG_fiber``.
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


    See :ref:`PEG_1chain-dataset` for description.
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
