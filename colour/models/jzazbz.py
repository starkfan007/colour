# -*- coding: utf-8 -*-
"""
:math:`J_za_zb_z` Colourspace
=============================

Defines the :math:`J_za_zb_z` colourspace:

-   :func:`colour.models.IZAZBZ_METHODS`
-   :func:`colour.models.XYZ_to_Izazbz`
-   :func:`colour.models.Izazbz_to_XYZ`
-   :func:`colour.XYZ_to_Jzazbz`
-   :func:`colour.Jzazbz_to_XYZ`

References
----------
-   :cite:`Safdar2017` : Safdar, M., Cui, G., Kim, Y. J., & Luo, M. R. (2017).
    Perceptually uniform color space for image signals including high dynamic
    range and wide gamut. Optics Express, 25(13), 15131.
    doi:10.1364/OE.25.015131
-   :cite:`Safdar2021` : Safdar, M., Hardeberg, J. Y., & Ronnier Luo, M.
    (2021). ZCAM, a colour appearance model based on a high dynamic range
    uniform colour space. Optics Express, 29(4), 6036. doi:10.1364/OE.413659
"""

import numpy as np

from colour.algebra import vector_dot
from colour.models.rgb.transfer_functions import (
    eotf_inverse_ST2084,
    eotf_ST2084,
)
from colour.models.rgb.transfer_functions.st_2084 import CONSTANTS_ST2084
from colour.utilities import (
    Structure,
    domain_range_scale,
    from_range_1,
    to_domain_1,
    tsplit,
    tstack,
    validate_method,
)
from colour.utilities.documentation import (
    DocstringTuple,
    is_documentation_building,
)
__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'CONSTANTS_JZAZBZ_SAFDAR2017',
    'CONSTANTS_JZAZBZ_SAFDAR2021',
    'MATRIX_JZAZBZ_XYZ_TO_LMS',
    'MATRIX_JZAZBZ_LMS_TO_XYZ',
    'MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2017',
    'MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2017',
    'MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2021',
    'MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2021',
    'IZAZBZ_METHODS',
    'XYZ_to_Izazbz',
    'Izazbz_to_XYZ',
    'XYZ_to_Jzazbz',
    'Jzazbz_to_XYZ',
]

CONSTANTS_JZAZBZ_SAFDAR2017 = Structure(
    b=1.15, g=0.66, d=-0.56, d_0=1.6295499532821566 * 10 ** -11)
CONSTANTS_JZAZBZ_SAFDAR2017.update(CONSTANTS_ST2084)
CONSTANTS_JZAZBZ_SAFDAR2017.m_2 = 1.7 * 2523 / 2 ** 5
"""
Constants for :math:`J_za_zb_z` colourspace and its variant of the perceptual
quantizer (PQ) from Dolby Laboratories.

Notes
-----
-   The :math:`m2` constant, i.e. the power factor has been re-optimized during
    the development of the :math:`J_za_zb_z` colourspace.

CONSTANTS_JZAZBZ_SAFDAR2017 : Structure
"""

CONSTANTS_JZAZBZ_SAFDAR2021 = Structure(**CONSTANTS_JZAZBZ_SAFDAR2017)
CONSTANTS_JZAZBZ_SAFDAR2021.d_0 = 3.7035226210190005 * 10 ** -11
"""
:math:`J_za_zb_z` colourspace constants for the *ZCAM* colour appearance model.

Notes
CONSTANTS_JZAZBZ_SAFDAR2021 : Structure
"""

MATRIX_JZAZBZ_XYZ_TO_LMS = np.array([
    [0.41478972, 0.579999, 0.0146480],
    [-0.2015100, 1.120649, 0.0531008],
    [-0.0166008, 0.264800, 0.6684799],
])
"""
:math:`J_za_zb_z` *CIE XYZ* tristimulus values to normalised cone responses
matrix.

MATRIX_JZAZBZ_XYZ_TO_LMS : array_like, (3, 3)
"""

MATRIX_JZAZBZ_LMS_TO_XYZ = np.linalg.inv(MATRIX_JZAZBZ_XYZ_TO_LMS)
"""
:math:`J_za_zb_z` normalised cone responses to *CIE XYZ* tristimulus values
matrix.

MATRIX_JZAZBZ_LMS_TO_XYZ : array_like, (3, 3)
"""

MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2017 = np.array([
    [0.500000, 0.500000, 0.000000],
    [3.524000, -4.066708, 0.542708],
    [0.199076, 1.096799, -1.295875],
])
"""
:math:`LMS_p` *SMPTE ST 2084:2014* encoded normalised cone responses to
:math:`I_za_zb_z` intermediate colourspace matrix.

MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2017 : array_like, (3, 3)
"""

MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2017 = np.linalg.inv(
    MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2017)
"""
:math:`I_za_zb_z` intermediate colourspace to :math:`LMS_p`
*SMPTE ST 2084:2014* encoded normalised cone responses matrix.

MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2017 : array_like, (3, 3)
"""

MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2021 = np.array([
    [0.000000, 1.000000, 0.000000],
    [3.524000, -4.066708, 0.542708],
    [0.199076, 1.096799, -1.295875],
])
"""
:math:`LMS_p` *SMPTE ST 2084:2014* encoded normalised cone responses to
:math:`I_za_zb_z` intermediate colourspace matrix.

References
----------
:cite:`Safdar2021`

MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2021 : array_like, (3, 3)
"""

MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2021 = np.linalg.inv(
    MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2021)
"""
:math:`I_za_zb_z` intermediate colourspace to :math:`LMS_p`
*SMPTE ST 2084:2014* encoded normalised cone responses matrix.

References
----------
:cite:`Safdar2021`

MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2021 : array_like, (3, 3)
"""

IZAZBZ_METHODS = ('Safdar 2017', 'Safdar 2021', 'ZCAM')
if is_documentation_building():  # pragma: no cover
    IZAZBZ_METHODS = DocstringTuple(IZAZBZ_METHODS)
    IZAZBZ_METHODS.__doc__ = """
Supported :math:`I_za_zb_z` computation methods.

References
----------
:cite:`Safdar2017`, :cite:`Safdar2021`

IZAZBZ_METHODS : tuple
    **{'Safdar 2017', 'Safdar 2021', 'ZCAM'}**
"""


def XYZ_to_Izazbz(XYZ_D65, constants=None, method='Safdar 2017'):
    """
    Converts from *CIE XYZ* tristimulus values to :math:`I_za_zb_z`
    colourspace.

    Parameters
    ----------
    XYZ_D65 : array_like
        *CIE XYZ* tristimulus values under
        *CIE Standard Illuminant D Series D65*.
    constants : Structure, optional
        :math:`J_za_zb_z` colourspace constants.
    method : unicode, optional
        **{'Safdar 2017', 'Safdar 2021', 'ZCAM'}**,
        Computation methods, *Safdar 2021* and *ZCAM* are equivalent.

    Returns
    -------
    ndarray
        :math:`I_za_zb_z` colourspace array where :math:`I_z` is the achromatic
        response, :math:`a_z` is redness-greenness and :math:`b_z` is
        yellowness-blueness.

    Warnings
    --------
    The underlying *SMPTE ST 2084:2014* transfer function is an absolute
    transfer function.

    Notes
    -----

    -   The underlying *SMPTE ST 2084:2014* transfer function is an absolute
        transfer function, thus the domain and range values for the *Reference*
        and *1* scales are only indicative that the data is not affected by
        scale transformations. The effective domain of *SMPTE ST 2084:2014*
        inverse electro-optical transfer function (EOTF / EOCF) is
        [0.0001, 10000].

    +------------+-----------------------+------------------+
    | **Domain** | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``XYZ``    | ``UN``                | ``UN``           |
    +------------+-----------------------+------------------+

    +------------+-----------------------+------------------+
    | **Range**  | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``Izazbz`` | ``Iz`` : [0, 1]       | ``Iz`` : [0, 1]  |
    |            |                       |                  |
    |            | ``az`` : [-1, 1]      | ``az`` : [-1, 1] |
    |            |                       |                  |
    |            | ``bz`` : [-1, 1]      | ``bz`` : [-1, 1] |
    +------------+-----------------------+------------------+

    References
    ----------
    :cite:`Safdar2017`, :cite:`Safdar2021`

    Examples
    --------
    >>> XYZ = np.array([0.20654008, 0.12197225, 0.05136952])
    >>> XYZ_to_Izazbz(XYZ)  # doctest: +ELLIPSIS
    array([ 0.0120779...,  0.0092430...,  0.0052600...])
    """

    X_D65, Y_D65, Z_D65 = tsplit(to_domain_1(XYZ_D65))

    method = validate_method(method, IZAZBZ_METHODS)

    if constants is None:
        if method == 'safdar 2017':
            constants = CONSTANTS_JZAZBZ_SAFDAR2017
        else:
            constants = CONSTANTS_JZAZBZ_SAFDAR2021

    X_p_D65 = constants.b * X_D65 - (constants.b - 1) * Z_D65
    Y_p_D65 = constants.g * Y_D65 - (constants.g - 1) * X_D65

    XYZ_p_D65 = tstack([X_p_D65, Y_p_D65, Z_D65])

    LMS = vector_dot(MATRIX_JZAZBZ_XYZ_TO_LMS, XYZ_p_D65)

    with domain_range_scale('ignore'):
        LMS_p = eotf_inverse_ST2084(LMS, 10000, constants)

    if method == 'safdar 2017':
        Izazbz = vector_dot(MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2017, LMS_p)
    else:
        Izazbz = vector_dot(MATRIX_JZAZBZ_LMS_P_TO_IZAZBZ_SAFDAR2021, LMS_p)
        Izazbz[..., 0] -= constants.d_0

    return from_range_1(Izazbz)


def Izazbz_to_XYZ(Izazbz, constants=None, method='Safdar 2017'):
    """
    Converts from :math:`I_za_zb_z` colourspace to *CIE XYZ* tristimulus
    values.

    Parameters
    ----------
    Izazbz : array_like
        :math:`I_za_zb_z` colourspace array where :math:`I_z` is the
        achromatic response, :math:`a_z` is redness-greenness and
        :math:`b_z` is yellowness-blueness.
    constants : Structure, optional
        :math:`J_za_zb_z` colourspace constants.
    method : unicode, optional
        **{'Safdar 2017', 'Safdar 2021', 'ZCAM'}**,
        Computation methods, *Safdar 2021* and *ZCAM* are equivalent.

    Returns
    -------
    ndarray
        *CIE XYZ* tristimulus values under
        *CIE Standard Illuminant D Series D65*.

    Warnings
    --------
    The underlying *SMPTE ST 2084:2014* transfer function is an absolute
    transfer function.

    Notes
    -----

    -   The underlying *SMPTE ST 2084:2014* transfer function is an absolute
        transfer function, thus the domain and range values for the *Reference*
        and *1* scales are only indicative that the data is not affected by
        scale transformations.

    +------------+-----------------------+------------------+
    | **Domain** | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``Izazbz`` | ``Iz`` : [0, 1]       | ``Iz`` : [0, 1]  |
    |            |                       |                  |
    |            | ``az`` : [-1, 1]      | ``az`` : [-1, 1] |
    |            |                       |                  |
    |            | ``bz`` : [-1, 1]      | ``bz`` : [-1, 1] |
    +------------+-----------------------+------------------+

    +------------+-----------------------+------------------+
    | **Range**  | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``XYZ``    | ``UN``                | ``UN``           |
    +------------+-----------------------+------------------+

    References
    ----------
    :cite:`Safdar2017`, :cite:`Safdar2021`

    Examples
    --------
    >>> Izazbz = np.array([0.01207793, 0.00924302, 0.00526007])
    >>> Izazbz_to_XYZ(Izazbz)  # doctest: +ELLIPSIS
    array([ 0.2065401...,  0.1219723...,  0.0513696...])
    """

    Izazbz = to_domain_1(Izazbz)

    method = validate_method(method, IZAZBZ_METHODS)

    if constants is None:
        if method == 'safdar 2017':
            constants = CONSTANTS_JZAZBZ_SAFDAR2017
        else:
            constants = CONSTANTS_JZAZBZ_SAFDAR2021

    if method == 'safdar 2017':
        LMS_p = vector_dot(MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2017, Izazbz)
    else:
        Izazbz[..., 0] += constants.d_0
        LMS_p = vector_dot(MATRIX_JZAZBZ_IZAZBZ_TO_LMS_P_SAFDAR2021, Izazbz)

    with domain_range_scale('ignore'):
        LMS = eotf_ST2084(LMS_p, 10000, constants)

    X_p_D65, Y_p_D65, Z_p_D65 = tsplit(
        vector_dot(MATRIX_JZAZBZ_LMS_TO_XYZ, LMS))

    X_D65 = (X_p_D65 + (constants.b - 1) * Z_p_D65) / constants.b
    Y_D65 = (Y_p_D65 + (constants.g - 1) * X_D65) / constants.g

    XYZ_D65 = tstack([X_D65, Y_D65, Z_p_D65])

    return from_range_1(XYZ_D65)


def XYZ_to_Jzazbz(XYZ_D65, constants=CONSTANTS_JZAZBZ_SAFDAR2017):
    """
    Converts from *CIE XYZ* tristimulus values to :math:`J_za_zb_z`
    colourspace.

    Parameters
    ----------
    XYZ_D65 : array_like
        *CIE XYZ* tristimulus values under
        *CIE Standard Illuminant D Series D65*.
    constants : Structure, optional
        :math:`J_za_zb_z` colourspace constants.

    Returns
    -------
    ndarray
        :math:`J_za_zb_z` colourspace array where :math:`J_z` is Lightness,
        :math:`a_z` is redness-greenness and :math:`b_z` is
        yellowness-blueness.

    Warnings
    --------
    The underlying *SMPTE ST 2084:2014* transfer function is an absolute
    transfer function.

    Notes
    -----

    -   The underlying *SMPTE ST 2084:2014* transfer function is an absolute
        transfer function, thus the domain and range values for the *Reference*
        and *1* scales are only indicative that the data is not affected by
        scale transformations. The effective domain of *SMPTE ST 2084:2014*
        inverse electro-optical transfer function (EOTF / EOCF) is
        [0.0001, 10000].

    +------------+-----------------------+------------------+
    | **Domain** | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``XYZ``    | ``UN``                | ``UN``           |
    +------------+-----------------------+------------------+

    +------------+-----------------------+------------------+
    | **Range**  | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``Jzazbz`` | ``Jz`` : [0, 1]       | ``Jz`` : [0, 1]  |
    |            |                       |                  |
    |            | ``az`` : [-1, 1]      | ``az`` : [-1, 1] |
    |            |                       |                  |
    |            | ``bz`` : [-1, 1]      | ``bz`` : [-1, 1] |
    +------------+-----------------------+------------------+

    References
    ----------
    :cite:`Safdar2017`

    Examples
    --------
    >>> XYZ = np.array([0.20654008, 0.12197225, 0.05136952])
    >>> XYZ_to_Jzazbz(XYZ)  # doctest: +ELLIPSIS
    array([ 0.0053504...,  0.0092430...,  0.0052600...])
    """

    XYZ_D65 = to_domain_1(XYZ_D65)

    with domain_range_scale('ignore'):
        I_z, a_z, b_z = tsplit(
            XYZ_to_Izazbz(XYZ_D65, CONSTANTS_JZAZBZ_SAFDAR2017, 'Safdar 2017'))

    J_z = ((1 + constants.d) * I_z) / (1 + constants.d * I_z) - constants.d_0

    Jzazbz = tstack([J_z, a_z, b_z])

    return from_range_1(Jzazbz)


def Jzazbz_to_XYZ(Jzazbz, constants=CONSTANTS_JZAZBZ_SAFDAR2017):
    """
    Converts from :math:`J_za_zb_z` colourspace to *CIE XYZ* tristimulus
    values.

    Parameters
    ----------
    Jzazbz : array_like
        :math:`J_za_zb_z` colourspace array  where :math:`J_z` is Lightness,
        :math:`a_z` is redness-greenness and :math:`b_z` is
        yellowness-blueness.
    constants : Structure, optional
        :math:`J_za_zb_z` colourspace constants.

    Returns
    -------
    ndarray
        *CIE XYZ* tristimulus values under
        *CIE Standard Illuminant D Series D65*.

    Warnings
    --------
    The underlying *SMPTE ST 2084:2014* transfer function is an absolute
    transfer function.

    Notes
    -----

    -   The underlying *SMPTE ST 2084:2014* transfer function is an absolute
        transfer function, thus the domain and range values for the *Reference*
        and *1* scales are only indicative that the data is not affected by
        scale transformations.

    +------------+-----------------------+------------------+
    | **Domain** | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``Jzazbz`` | ``Jz`` : [0, 1]       | ``Jz`` : [0, 1]  |
    |            |                       |                  |
    |            | ``az`` : [-1, 1]      | ``az`` : [-1, 1] |
    |            |                       |                  |
    |            | ``bz`` : [-1, 1]      | ``bz`` : [-1, 1] |
    +------------+-----------------------+------------------+

    +------------+-----------------------+------------------+
    | **Range**  | **Scale - Reference** | **Scale - 1**    |
    +============+=======================+==================+
    | ``XYZ``    | ``UN``                | ``UN``           |
    +------------+-----------------------+------------------+

    References
    ----------
    :cite:`Safdar2017`

    Examples
    --------
    >>> Jzazbz = np.array([0.00535048, 0.00924302, 0.00526007])
    >>> Jzazbz_to_XYZ(Jzazbz)  # doctest: +ELLIPSIS
    array([ 0.2065402...,  0.1219723...,  0.0513696...])
    """

    J_z, a_z, b_z = tsplit(to_domain_1(Jzazbz))

    I_z = ((J_z + constants.d_0) / (1 + constants.d - constants.d *
                                    (J_z + constants.d_0)))

    with domain_range_scale('ignore'):
        XYZ_D65 = Izazbz_to_XYZ(
            tstack([I_z, a_z, b_z]), CONSTANTS_JZAZBZ_SAFDAR2017,
            'Safdar 2017')

    return from_range_1(XYZ_D65)
