# -*- coding: utf-8 -*-

"""Short peptide inside a pure DMPC membrane without water.

https://figshare.com/articles/Short_molecular_dynamics_of_a_peptide_inside_a_pure_DMPC_membrane/8046437
"""

from os.path import dirname, exists, join
from os import makedirs, remove

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

NAME = "membrane_peptide"
DESCRIPTION = "membrane_peptide.rst"
# The original data can be found at the figshare URL.
# The SHA256 checksum of the zip file changes with every download so we
# cannot check its checksum. Instead we download individual files.
# separately. The keys of this dict are also going to be the keys in the
# Bunch that is returned.
ARCHIVE = {
    'topology': RemoteFileMetadata(
        filename='memb_pept.tpr',
        url='https://ndownloader.figshare.com/files/14993171',
        checksum='677a3ae55e35c24f37f2610eafa92d19285d1774731d6ffb9a99dfde39b8c437',
    ),
    'trajectory':  RemoteFileMetadata(
        filename='memb_pept.xtc',
        url='https://ndownloader.figshare.com/files/14993174',
        checksum='f9bdfee4e1aa69ccfeef21cb74703202f6728f514543c4125382bd5250773eb7',
    ),
}

logger = logging.getLogger(__name__)


def fetch_membrane_peptide(data_home=None, download_if_missing=True):
    """Load the helical peptide in DMPC membrane equilibrium trajectory

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/membrane_peptide``.
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


    See :ref:`membrane-peptide-dataset` for description.
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
