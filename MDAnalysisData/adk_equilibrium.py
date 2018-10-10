# -*- coding: utf-8 -*-

"""AdK equilibrium trajectory without water.

https://figshare.com/articles/Molecular_dynamics_trajectory_for_benchmarking_MDAnalysis/5108170/1
"""

import logging

from .base import RemoteFileMetadata, Dataset


logger = logging.getLogger(__name__)


class ADK_Equilibrium(Dataset):
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
