# -*- coding: utf-8 -*-

"""Large vesicles library (coarse grained).

https://figshare.com/articles/Large_System_Vesicle_Benchmark_Library/3406708
"""


from os.path import dirname, exists, join
from os import makedirs, remove
import tarfile

import logging

from .base import get_data_home
from .base import _fetch_remote, _read_description
from .base import RemoteFileMetadata
from .base import Bunch

METADATA = {
    'vesicle_lib': {
        'NAME': "vesicle_library",
        'DESCRIPTION': "vesicle_lib.rst",
        'ARCHIVE': {
            'tarfile': RemoteFileMetadata(
                filename='vesicles_1.0.tar.bz2',
                url='https://ndownloader.figshare.com/files/5320846',
                checksum='cba5a6221df664c79229a27d82faf779f63dee608f96a7b3b64ef209b93ec0d0',
            ),
        },
        'CONTENTS': {
            'structures': ["vesicles/1_75M/system.gro",
                           "vesicles/3_5M/system.gro",
                           "vesicles/10M/system.gro"],
            'labels': ["1_75M", "3_5M", "10M"],
            'N_structures': 3,
        },
    },
}

logger = logging.getLogger(__name__)

def fetch_vesicle_lib(data_home=None, download_if_missing=True):
    """Load the vesicle library dataset

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all MDAnalysisData data is stored in '~/MDAnalysis_data' subfolders.
        This dataset is stored in ``<data_home>/vesicle_library``.
    download_if_missing : optional, default=True
        If ``False``, raise a :exc:`IOError` if the data is not locally available
        instead of trying to download the data from the source site.

    Returns
    -------
    dataset : dict-like object with the following attributes:
    dataset.structures : list
        list with filenames of the different vesicle systems (in
        GRO format)
    dataset.N_structures : int
        number of structures
    dataset.labels : list
        descriptors of the files in `dataset.structures` (same order), giving
        their approximate sizes in number of particles
    dataset.DESCR : string
        Description of the ensemble


    See :ref:`vesicle-library-dataset` for description.
    """
    metadata = METADATA['vesicle_lib']
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

    records.structures = [join(data_location, path) for path in metadata['CONTENTS']['structures']
                          if exists(join(data_location, path))]
    records.N_structures = metadata['CONTENTS']['N_structures']
    records.labels = metadata['CONTENTS']['labels']
    if len(records.structures) != records.N_structures:
        # should not happen...
        raise RuntimeError("structure files in {0} are incomplete: only {1} "
                           "but should be {2}.".format(
                               metadata['CONTENTS']['structures'],
                               len(records.structures),
                               records.N_structures))

    records.DESCR = _read_description(metadata['DESCRIPTION'])

    return records
