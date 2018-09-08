# -*- coding: utf-8 -*-

"""AdK equilibrium trajectory without water

The original dataset is available from doi
`10.6084/m9.figshare.5108170.v1
<https://doi.org/10.6084/m9.figshare.5108170.v1>`_

   https://figshare.com/articles/Molecular_dynamics_trajectory_for_benchmarking_MDAnalysis/5108170

MD trajectory of apo adenylate kinase with CHARMM27 force field and
simulated with explicit water and ions in NPT at 300 K and 1
bar. Saved every 240 ps for a total of 1.004 µs. Produced on PSC
Anton. The trajectory only contains the protein and all solvent
stripped. Superimposed on the CORE domain of AdK by RMSD fitting.

The topology is contained in the PSF file (CHARMM format). The
trajectory is contained in the DCD file (CHARMM/NAMD format).


References
----------

Seyler, Sean; Beckstein, Oliver (2017): Molecular dynamics trajectory for benchmarking MDAnalysis. figshare. Fileset. `10.6084/m9.figshare.5108170.v1
<https://doi.org/10.6084/m9.figshare.5108170.v1>`_
"""

# Authors: Oliver Beckstein, Sean L. Seyler
# License: CC-BY 4.0

from os.path import dirname, exists, join
from os import makedirs, remove
import zipfile
import codecs

import logging

from .base import get_data_home
from .base import _fetch_remote
from .base import RemoteFileMetadata
from .base import Bunch

# The original data can be found at the figshare URL
ARCHIVE = RemoteFileMetadata(
    filename='adk_equilibrium.zip',
    url='https://ndownloader.figshare.com/articles/5108170/versions/1',
    checksum=('03c0cb53ec743680a3feecfedd7acbd38e66d6a87e09de33a83271bb9e6c3e95',)  # sha256
)

logger = logging.getLogger(__name__)


def fetch_adk_equilibrium(data_home=None, download_if_missing=True):
    """Load the AdK 1us equilibrium trajectory (without water)

    Parameters
    ----------
    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all scikit-learn data is stored in '~/mdanalysis_data' subfolders.
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
    name = "adk_equilibrium"
    data_location = join(get_data_home(data_home=data_home),
                             name)
    if not exists(data_location):
        makedirs(data_location)

    topology = join(data_location, 'adk4AKE.psf')
    trajectory = join(data_location, '1ake_007-nowater-core-dt240ps.dcd')

    if not exists(topology) and not exists(trajectory):
        if not download_if_missing:
            raise IOError("Data not found and `download_if_missing` is False")

        logger.info('Downloading "AdK equilibrium" dataset from {} to {}'.format(
            ARCHIVE.url, data_location))

        archive_path = _fetch_remote(ARCHIVE, dirname=data_location)

        with zipfile.ZipFile(archive_path, mode="r") as z:
            z.extractall(path=data_location)
        remove(archive_path)

    module_path = dirname(__file__)
    with codecs.open(join(module_path, 'descr', 'adk_equilibrium.rst')) as dfile:
        descr = dfile.read()

    return Bunch(topology=topology,
                 trajectory=trajectory,
                 DESCR=descr)
