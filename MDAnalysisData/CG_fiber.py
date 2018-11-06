# -*- coding: utf-8 -*-

"""Coarse-grained molecular dynamics of an amphiphilic fiber.

https://figshare.com/articles/126chains_dcd/7259915
"""

from os.path import dirname, exists, join
from os import makedirs, remove

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "CG_fiber"
DESCRIPTION = "CG_fiber.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'topology': RemoteFileMetadata(
        filename='126chains.psf',
        url='https://ndownloader.figshare.com/files/13374146',
        checksum='3ddb654b68549ac2ad5107a4282899f41fad233d09ea572446031711af4e57da',
    ),
    'trajectory':  RemoteFileMetadata(
        filename='126chains.dcd',
        url='https://ndownloader.figshare.com/files/13375838',
        checksum='e0b47d422f31ec209ea810edcf6cf3830da04bb2e1540f520477c27f4433d849',
    ),
}

logger = logging.getLogger(__name__)


def fetch_CG_fiber(data_home=None, download_if_missing=True):
    """Load the CG fiber self-assembly trajectory

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


    See :ref:`CG_fiber-dataset` for description.
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
