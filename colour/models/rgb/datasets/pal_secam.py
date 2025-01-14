# -*- coding: utf-8 -*-
"""
Pal/Secam Colourspace
=====================

Defines the *Pal/Secam* colourspace:

-   :attr:`colour.models.RGB_COLOURSPACE_PAL_SECAM`.

References
----------
-   :cite:`InternationalTelecommunicationUnion1998a` : International
    Telecommunication Union. (1998). Recommendation ITU-R BT.470-6 -
    CONVENTIONAL TELEVISION SYSTEMS (pp. 1-36).
    http://www.itu.int/dms_pubrec/itu-r/rec/bt/\
R-REC-BT.470-6-199811-S!!PDF-E.pdf
"""

from colour.models.rgb import RGB_Colourspace
from colour.models.rgb.datasets.itur_bt_470 import (
    PRIMARIES_BT470_625,
    CCS_WHITEPOINT_BT470_625,
    WHITEPOINT_NAME_BT470_625,
    MATRIX_BT470_625_TO_XYZ,
    MATRIX_XYZ_TO_BT470_625,
    RGB_COLOURSPACE_BT470_625,
)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'PRIMARIES_PAL_SECAM',
    'WHITEPOINT_NAME_PAL_SECAM',
    'CCS_WHITEPOINT_PAL_SECAM',
    'MATRIX_PAL_SECAM_TO_XYZ',
    'MATRIX_XYZ_TO_PAL_SECAM',
    'RGB_COLOURSPACE_PAL_SECAM',
]

PRIMARIES_PAL_SECAM = PRIMARIES_BT470_625
"""
*Pal/Secam* colourspace primaries.

PRIMARIES_PAL_SECAM : ndarray, (3, 2)
"""

WHITEPOINT_NAME_PAL_SECAM = WHITEPOINT_NAME_BT470_625
"""
*Pal/Secam* colourspace whitepoint name.

WHITEPOINT_NAME_PAL_SECAM : str
"""

CCS_WHITEPOINT_PAL_SECAM = CCS_WHITEPOINT_BT470_625
"""
*Pal/Secam* colourspace whitepoint chromaticity coordinates.

CCS_WHITEPOINT_PAL_SECAM : ndarray
"""

MATRIX_PAL_SECAM_TO_XYZ = MATRIX_BT470_625_TO_XYZ
"""
*Pal/Secam* colourspace to *CIE XYZ* tristimulus values matrix.

MATRIX_PAL_SECAM_TO_XYZ : array_like, (3, 3)
"""

MATRIX_XYZ_TO_PAL_SECAM = MATRIX_XYZ_TO_BT470_625
"""
*CIE XYZ* tristimulus values to *Pal/Secam* colourspace matrix.

MATRIX_XYZ_TO_PAL_SECAM : array_like, (3, 3)
"""

RGB_COLOURSPACE_PAL_SECAM = RGB_Colourspace(
    'Pal/Secam',
    PRIMARIES_PAL_SECAM,
    CCS_WHITEPOINT_PAL_SECAM,
    WHITEPOINT_NAME_PAL_SECAM,
    MATRIX_PAL_SECAM_TO_XYZ,
    MATRIX_XYZ_TO_PAL_SECAM,
    RGB_COLOURSPACE_BT470_625.cctf_encoding,
    RGB_COLOURSPACE_BT470_625.cctf_decoding,
)
RGB_COLOURSPACE_PAL_SECAM.__doc__ = """
*Pal/Secam* colourspace.

References
----------
:cite:`InternationalTelecommunicationUnion1998a`

RGB_COLOURSPACE_PAL_SECAM : RGB_Colourspace
"""
