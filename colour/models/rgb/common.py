# -*- coding: utf-8 -*-
"""
Common RGB Colour Models Utilities
==================================

Defines various RGB colour models common utilities.
"""

from colour.colorimetry import CCS_ILLUMINANTS
from colour.models.rgb import RGB_COLOURSPACES, RGB_to_XYZ, XYZ_to_RGB

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'XYZ_to_sRGB',
    'sRGB_to_XYZ',
]


def XYZ_to_sRGB(XYZ,
                illuminant=CCS_ILLUMINANTS[
                    'CIE 1931 2 Degree Standard Observer']['D65'],
                chromatic_adaptation_transform='CAT02',
                apply_cctf_encoding=True):
    """
    Converts from *CIE XYZ* tristimulus values to *sRGB* colourspace.

    Parameters
    ----------
    XYZ : array_like
        *CIE XYZ* tristimulus values.
    illuminant : array_like, optional
        Source illuminant chromaticity coordinates.
    chromatic_adaptation_transform : str, optional
        **{'CAT02', 'XYZ Scaling', 'Von Kries', 'Bradford', 'Sharp',
        'Fairchild', 'CMCCAT97', 'CMCCAT2000', 'CAT02 Brill 2008', 'CAT16',
        'Bianco 2010', 'Bianco PC 2010'}**,
        *Chromatic adaptation* transform.
    apply_cctf_encoding : bool, optional
        Apply *sRGB* encoding colour component transfer function /
        opto-electronic transfer function.

    Returns
    -------
    ndarray
        *sRGB* colour array.

    Notes
    -----

    +------------+-----------------------+---------------+
    | **Domain** | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``XYZ``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    +------------+-----------------------+---------------+
    | **Range**  | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``RGB``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    Examples
    --------
    >>> import numpy as np
    >>> XYZ = np.array([0.20654008, 0.12197225, 0.05136952])
    >>> XYZ_to_sRGB(XYZ)  # doctest: +ELLIPSIS
    array([ 0.7057393...,  0.1924826...,  0.2235416...])
    """

    sRGB = RGB_COLOURSPACES['sRGB']

    return XYZ_to_RGB(
        XYZ,
        illuminant,
        sRGB.whitepoint,
        sRGB.matrix_XYZ_to_RGB,
        chromatic_adaptation_transform,
        sRGB.cctf_encoding if apply_cctf_encoding else None,
    )


def sRGB_to_XYZ(RGB,
                illuminant=CCS_ILLUMINANTS[
                    'CIE 1931 2 Degree Standard Observer']['D65'],
                chromatic_adaptation_transform='CAT02',
                apply_cctf_decoding=True):
    """
    Converts from *sRGB* colourspace to *CIE XYZ* tristimulus values.

    Parameters
    ----------
    RGB : array_like
        *sRGB* colourspace array.
    illuminant : array_like, optional
        Source illuminant chromaticity coordinates.
    chromatic_adaptation_transform : str, optional
        **{'CAT02', 'XYZ Scaling', 'Von Kries', 'Bradford', 'Sharp',
        'Fairchild', 'CMCCAT97', 'CMCCAT2000', 'CAT02 Brill 2008', 'CAT16',
        'Bianco 2010', 'Bianco PC 2010'}**,
        *Chromatic adaptation* transform.
    apply_cctf_decoding : bool, optional
        Apply *sRGB* decoding colour component transfer function  /
        electro-optical transfer function.

    Returns
    -------
    ndarray
        *CIE XYZ* tristimulus values.

    Notes
    -----

    +------------+-----------------------+---------------+
    | **Domain** | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``RGB``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    +------------+-----------------------+---------------+
    | **Range**  | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``XYZ``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    Examples
    --------
    >>> import numpy as np
    >>> RGB = np.array([0.70573936, 0.19248266, 0.22354169])
    >>> sRGB_to_XYZ(RGB)  # doctest: +ELLIPSIS
    array([ 0.2065429...,  0.1219794...,  0.0513714...])
    """

    sRGB = RGB_COLOURSPACES['sRGB']

    return RGB_to_XYZ(
        RGB,
        sRGB.whitepoint,
        illuminant,
        sRGB.matrix_RGB_to_XYZ,
        chromatic_adaptation_transform,
        sRGB.cctf_decoding if apply_cctf_decoding else None,
    )
