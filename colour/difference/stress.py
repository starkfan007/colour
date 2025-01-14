# -*- coding: utf-8 -*-
"""
Standardized Residual Sum of Squares (STRESS) Index
===================================================

Defines the *Kruskal's Standardized Residual Sum of Squares (:math:`STRESS`)*
index:

-   :func:`colour.index_stress_Garcia2007`: :math:`STRESS` index computation
    according to *García, Huertas, Melgosa and Cui (2007)* method.
-   :func:`colour.index_stress`: *Lightness* :math:`STRESS` index computation
    according to given method.

References
----------
-   :cite:`Garcia2007` : García, P. A., Huertas, R., Melgosa, M., & Cui, G.
    (2007). Measurement of the relationship between perceived and computed
    color differences. Journal of the Optical Society of America A, 24(7),
    1823. doi:10.1364/JOSAA.24.001823
"""

import numpy as np

from colour.utilities import CaseInsensitiveMapping, validate_method

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'index_stress_Garcia2007',
    'INDEX_STRESS_METHODS',
    'index_stress',
]


def index_stress_Garcia2007(d_E, d_V):
    """
    Computes the
    *Kruskal's Standardized Residual Sum of Squares (:math:`STRESS`)*
    index according to *García, Huertas, Melgosa and Cui (2007)* method.

    Parameters
    ----------
    d_E : array_like
        Computed colour difference array :math:`\\Delta E`.
    d_V : array_like
        Computed colour difference array :math:`\\Delta V`.

    Returns
    -------
    numeric or ndarray
        :math:`STRESS` index.

    References
    ----------
    :cite:`Garcia2007`

    Examples
    --------
    >>> d_E = np.array([2.0425, 2.8615, 3.4412])
    >>> d_V = np.array([1.2644, 1.2630, 1.8731])
    >>> index_stress_Garcia2007(d_E, d_V)  # doctest: +ELLIPSIS
    0.1211709...
    """

    F_1 = np.sum(d_E ** 2) / np.sum(d_E * d_V)

    stress = np.sqrt(
        np.sum((d_E - F_1 * d_V) ** 2) / np.sum(F_1 ** 2 * d_V ** 2))

    return stress


INDEX_STRESS_METHODS = CaseInsensitiveMapping({
    'Garcia 2007': index_stress_Garcia2007,
})
INDEX_STRESS_METHODS.__doc__ = """
Supported :math:`STRESS` index computation methods.

References
----------
:cite:`Garcia2007`

INDEX_STRESS_METHODS : CaseInsensitiveMapping
    **{'Garcia 2007'}**
"""


def index_stress(d_E, d_V, method='Garcia 2007'):
    """
    Computes the
    *Kruskal's Standardized Residual Sum of Squares (:math:`STRESS`)*
    index according to given method.

    Parameters
    ----------
    d_E : array_like
        Computed colour difference array :math:`\\Delta E`.
    d_V : array_like
        Computed colour difference array :math:`\\Delta V`.
    method : str, optional
        **{'Garcia 2007'}**,
        Computation method.

    Returns
    -------
    numeric or ndarray
        :math:`STRESS` index.

    References
    ----------
    :cite:`Garcia2007`

    Examples
    --------
    >>> d_E = np.array([2.0425, 2.8615, 3.4412])
    >>> d_V = np.array([1.2644, 1.2630, 1.8731])
    >>> index_stress(d_E, d_V)  # doctest: +ELLIPSIS
    0.1211709...
    """

    method = validate_method(method, INDEX_STRESS_METHODS)

    function = INDEX_STRESS_METHODS[method]

    return function(d_E, d_V)
