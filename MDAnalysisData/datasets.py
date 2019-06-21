"""Access to all datasets via ``fetch_*()`` functions.

"""
# import load_* and fetch_* functions from modules

from __future__ import absolute_import


from .base import get_data_home, clear_data_home
from .adk_equilibrium import fetch_adk_equilibrium
from .adk_transitions import (fetch_adk_transitions_DIMS,
                              fetch_adk_transitions_FRODA)
from .nhaa_equilibrium import fetch_nhaa_equilibrium
from .ifabp_water import fetch_ifabp_water
from .vesicles import fetch_vesicle_lib
from .CG_fiber import fetch_CG_fiber
from .PEG_1chain import fetch_PEG_1chain
from .membrane_peptide import fetch_membrane_peptide
from .yiip_equilibrium import (fetch_yiip_equilibrium_short,
                               fetch_yiip_equilibrium_long)

__all__ = [
    'get_data_home',
    'clear_data_home',
    'fetch_adk_equilibrium',
    'fetch_adk_transitions_DIMS',
    'fetch_adk_transitions_FRODA',
    'fetch_ifabp_water',
    'fetch_vesicle_lib'
    'fetch_nhaa_equilibrium',
    'fetch_CG_fiber',
    'fetch_PEG_1chain',
    'fetch_membrane_peptide',
    'fetch_yiip_equilibrium_short',
    'fetch_yiip_equilibrium_long',
]
