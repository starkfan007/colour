# -*- coding: utf-8 -*-
"""
ANSI/IES TM-30-18 Colour Rendition Report Components
====================================================

Defines the *ANSI/IES TM-30-18 Colour Rendition Report* components plotting
objects:

-   :func:`colour.plotting.tm3018.components.plot_spectra_ANSIIESTM3018`
-   :func:`colour.plotting.tm3018.components.plot_colour_vector_graphic`
-   :func:`colour.plotting.tm3018.components.plot_16_bin_bars`
-   :func:`colour.plotting.tm3018.components.plot_local_chroma_shifts`
-   :func:`colour.plotting.tm3018.components.plot_local_hue_shifts`
-   :func:`colour.plotting.tm3018.components.plot_local_colour_fidelities`
-   :func:`colour.plotting.tm3018.components.plot_colour_fidelity_indexes`
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from colour.colorimetry import sd_to_XYZ
from colour.io import read_image
from colour.utilities import as_float_array
from colour.plotting import (
    CONSTANTS_COLOUR_STYLE,
    artist,
    override_style,
    plot_image,
    render,
)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'RESOURCES_DIRECTORY_ANSIIESTM3018',
    'plot_spectra_ANSIIESTM3018',
    'plot_colour_vector_graphic',
    'plot_16_bin_bars',
    'plot_local_chroma_shifts',
    'plot_local_hue_shifts',
    'plot_local_colour_fidelities',
    'plot_colour_fidelity_indexes',
]

RESOURCES_DIRECTORY_ANSIIESTM3018 = os.path.join(
    os.path.dirname(__file__), 'resources')
"""
Resources directory.

RESOURCES_DIRECTORY_ANSIIESTM3018 : str
"""

_BIN_BAR_COLOURS = [
    '#A35C60', '#CC765E', '#CC8145', '#D8AC62', '#AC9959', '#919E5D',
    '#668B5E', '#61B290', '#7BBAA6', '#297A7E', '#55788D', '#708AB2',
    '#988CAA', '#735877', '#8F6682', '#BA7A8E'
]

_BIN_ARROW_COLOURS = [
    '#E62828', '#E74B4B', '#FB812E', '#FFB529', '#CBCA46', '#7EB94C',
    '#41C06D', '#009C7C', '#16BCB0', '#00A4BF', '#0085C3', '#3B62AA',
    '#4568AE', '#6A4E85', '#9D69A1', '#A74F81'
]

_TCS_BAR_COLOURS = [
    '#F1BDCD', '#CA6183', '#573A40', '#CD8791', '#AD3F55', '#925F62',
    '#933440', '#8C3942', '#413D3E', '#FA8070', '#C35644', '#DA604A',
    '#824E39', '#BCA89F', '#C29A89', '#8D593C', '#915E3F', '#99745B',
    '#D39257', '#D07F2C', '#FEB45F', '#EFA248', '#F0DFBD', '#FED586',
    '#D0981E', '#FED06A', '#B5AC81', '#645D37', '#EAD163', '#9E9464',
    '#EBD969', '#C4B135', '#E6DE9C', '#99912C', '#61603A', '#C2C2AF',
    '#6D703B', '#D2D7A1', '#4B5040', '#6B7751', '#D3DCC3', '#88B33A',
    '#8EBF3E', '#3E3F3D', '#65984A', '#83A96E', '#92AE86', '#91CD8E',
    '#477746', '#568C6A', '#659477', '#276E49', '#008D62', '#B6E2D4',
    '#A5D9CD', '#39C4AD', '#00A18A', '#009786', '#B4E1D9', '#CDDDDC',
    '#99C1C0', '#909FA1', '#494D4E', '#009FA8', '#32636A', '#007788',
    '#007F95', '#66A0B2', '#687D88', '#75B6DB', '#1E5574', '#AAB9C3',
    '#3091C4', '#3B3E41', '#274D72', '#376FB8', '#496692', '#3B63AC',
    '#A0AED5', '#9293C8', '#61589D', '#D4D3E5', '#ACA6CA', '#3E3B45',
    '#5F5770', '#A08CC7', '#664782', '#A77AB5', '#6A4172', '#7D4983',
    '#C4BFC4', '#937391', '#AE91AA', '#764068', '#BF93B1', '#D7A9C5',
    '#9D587F', '#CE6997', '#AE4A79'
]


@override_style()
def plot_spectra_ANSIIESTM3018(specification, **kwargs):
    """
    Plots a comparison of the spectral distributions of a test emission source
    and a reference illuminant for *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    specification : ColourQuality_Specification_ANSIIESTM3018
        *ANSI/IES TM-30-18 Colour Rendition Report* specification.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> from colour import SDS_ILLUMINANTS
    >>> from colour.quality import colour_fidelity_index_ANSIIESTM3018
    >>> sd = SDS_ILLUMINANTS['FL2']
    >>> specification = colour_fidelity_index_ANSIIESTM3018(sd, True)
    >>> plot_spectra_ANSIIESTM3018(specification)
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    settings = kwargs.copy()

    _figure, axes = artist(**settings)

    Y_reference = sd_to_XYZ(specification.sd_reference)[1]
    Y_test = sd_to_XYZ(specification.sd_test)[1]

    axes.plot(
        specification.sd_reference.wavelengths,
        specification.sd_reference.values / Y_reference,
        'black',
        label='Reference')
    axes.plot(
        specification.sd_test.wavelengths,
        specification.sd_test.values / Y_test,
        '#F05046',
        label='Test')
    axes.tick_params(axis='y', which='both', length=0)
    axes.set_yticklabels([])

    settings = {
        'axes': axes,
        'legend': True,
        'legend_columns': 2,
        'x_label': 'Wavelength (nm)',
        'y_label': 'Radiant Power\n(Equal Luminous Flux)',
    }
    settings.update(kwargs)

    return render(**settings)


def plot_colour_vector_graphic(specification, **kwargs):
    """
    Plots *Color Vector Graphic* according to
    *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    specification : ColourQuality_Specification_ANSIIESTM3018
        *ANSI/IES TM-30-18 Colour Rendition Report* specification.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> from colour import SDS_ILLUMINANTS
    >>> from colour.quality import colour_fidelity_index_ANSIIESTM3018
    >>> sd = SDS_ILLUMINANTS['FL2']
    >>> specification = colour_fidelity_index_ANSIIESTM3018(sd, True)
    >>> plot_colour_vector_graphic(specification)
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    settings = kwargs.copy()
    settings['standalone'] = False

    # Background
    background_image = read_image(
        os.path.join(RESOURCES_DIRECTORY_ANSIIESTM3018, 'CVG_Background.jpg'))
    _figure, axes = plot_image(
        background_image,
        imshow_kwargs={'extent': [-1.5, 1.5, -1.5, 1.5]},
        **settings)

    # Lines dividing the hues in 16 equal parts along with bin numbers.
    axes.plot(0, 0, '+', color='#A6A6A6')
    for i in range(16):
        angle = 2 * np.pi * i / 16
        dx = np.cos(angle)
        dy = np.sin(angle)
        axes.plot(
            (0.15 * dx, 1.5 * dx), (0.15 * dy, 1.5 * dy),
            '--',
            color='#A6A6A6',
            lw=0.75)

        angle = 2 * np.pi * (i + 0.5) / 16
        axes.annotate(
            str(i + 1),
            color='#A6A6A6',
            ha='center',
            va='center',
            xy=(1.41 * np.cos(angle), 1.41 * np.sin(angle)),
            weight='bold',
            size=9)

    # Circles.
    circle = plt.Circle((0, 0), 1, color='black', lw=1.25, fill=False)
    axes.add_artist(circle)
    for radius in [0.8, 0.9, 1.1, 1.2]:
        circle = plt.Circle((0, 0), radius, color='white', lw=0.75, fill=False)
        axes.add_artist(circle)

    # -/+20% marks near the white circles.
    props = dict(ha='right', color='white', size=7)
    axes.annotate('-20%', xy=(0, -0.8), va='bottom', **props)
    axes.annotate('+20%', xy=(0, -1.2), va='top', **props)

    # Average "CAM02" h correlate for each bin, in radians.
    average_hues = as_float_array([
        np.mean([
            specification.colorimetry_data[1][i].CAM.h
            for i in specification.bins[j]
        ]) for j in range(16)
    ]) / 180 * np.pi
    xy_reference = np.transpose(
        np.vstack([np.cos(average_hues),
                   np.sin(average_hues)]))

    # Arrow offsets as defined by the standard.
    offsets = ((specification.averages_test - specification.averages_reference)
               / specification.average_norms[:, np.newaxis])
    xy_test = xy_reference + offsets

    # Arrows.
    for i in range(16):
        axes.arrow(
            xy_reference[i, 0],
            xy_reference[i, 1],
            offsets[i, 0],
            offsets[i, 1],
            length_includes_head=True,
            width=0.005,
            head_width=0.04,
            linewidth=None,
            color=_BIN_ARROW_COLOURS[i])

    # Red (test) gamut shape.
    loop = np.append(xy_test, xy_test[0, np.newaxis], axis=0)
    axes.plot(loop[:, 0], loop[:, 1], '-', color='#F05046', lw=2)

    def corner_label_and_text(label, text, ha, va):
        """
        Draws a label and text in given corner.
        """

        x = -1.45 if ha == 'left' else 1.45
        y = 1.45 if va == 'top' else -1.45
        y_text = -15 if va == 'top' else 15

        axes.annotate(
            text,
            xy=(x, y),
            color='black',
            ha=ha,
            va=va,
            weight='bold',
            size='larger')
        axes.annotate(
            label,
            xy=(x, y),
            color='black',
            xytext=(0, y_text),
            textcoords='offset points',
            ha=ha,
            va=va,
            size='small')

    corner_label_and_text('$R_f$', '{0:.0f}'.format(specification.R_f), 'left',
                          'top')
    corner_label_and_text('$R_g$', '{0:.0f}'.format(specification.R_g),
                          'right', 'top')
    corner_label_and_text('CCT', '{0:.0f} K'.format(specification.CCT), 'left',
                          'bottom')
    corner_label_and_text('$D_{uv}$', '{0:.4f}'.format(specification.D_uv),
                          'right', 'bottom')

    settings = {'standalone': True}
    settings.update(kwargs)

    return render(**settings)


def plot_16_bin_bars(values,
                     label_template,
                     x_ticker=False,
                     label_orientation='Vertical',
                     **kwargs):
    """
    Plots the 16 bin bars for given values according to
    *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    values : array_like
        Values to generate the bin bars for.
    label_template : str
        Template to format the labels.
    x_ticker : bool, optional
        Whether to show the *X* axis ticker and the associated label.
    label_orientation : str, optional
        **{'Vertical', 'Horizonal'}**,
        Orientation of the labels.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> plot_16_bin_bars(np.arange(16), '{0}')
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    _figure, axes = artist(**kwargs)

    bar_count = len(_BIN_BAR_COLOURS)
    axes.bar(
        np.arange(bar_count) + 1,
        values,
        color=_BIN_BAR_COLOURS,
        width=1,
        edgecolor='black',
        linewidth=CONSTANTS_COLOUR_STYLE.geometry.short / 3)
    axes.set_xlim(0.5, bar_count + 0.5)
    if x_ticker:
        axes.set_xticks(np.arange(1, bar_count + 1))
        axes.set_xlabel('Hue-Angle Bin (j)')
    else:
        axes.set_xticks([])

    label_orientation = label_orientation.lower()
    value_max = max(values)
    for i, value in enumerate(values):
        if label_orientation == 'vertical':
            va, vo = (('bottom', value_max * 0.15)
                      if value > 0 else ('top', -value_max * 0.15))
            axes.annotate(
                label_template.format(value),
                xy=(i + 1, value + vo),
                rotation=90,
                fontsize='xx-small',
                ha='center',
                va=va)
        elif label_orientation == 'horizontal':
            va, vo = (('bottom', value_max * 0.025)
                      if value < 90 else ('top', -value_max * 0.025))
            axes.annotate(
                label_template.format(value),
                xy=(i + 1, value + vo),
                fontsize='xx-small',
                ha='center',
                va=va)

    return render(**kwargs)


def plot_local_chroma_shifts(specification, x_ticker=False, **kwargs):
    """
    Plots the local chroma shifts according to
    *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    specification : ColourQuality_Specification_ANSIIESTM3018
        *ANSI/IES TM-30-18 Colour Rendition Report* specification.
    x_ticker : bool, optional
        Whether to show the *X* axis ticker and the associated label.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> from colour import SDS_ILLUMINANTS
    >>> from colour.quality import colour_fidelity_index_ANSIIESTM3018
    >>> sd = SDS_ILLUMINANTS['FL2']
    >>> specification = colour_fidelity_index_ANSIIESTM3018(sd, True)
    >>> plot_local_chroma_shifts(specification)
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    settings = kwargs.copy()
    settings['standalone'] = False

    _figure, axes = plot_16_bin_bars(specification.R_cs, '{0:.0f}%', x_ticker,
                                     **settings)

    axes.set_ylim(-40, 40)
    axes.set_ylabel('Local Chroma Shift ($R_{cs,hj}$)')

    ticks = np.arange(-40, 41, 10)
    axes.set_yticks(ticks)
    axes.set_yticklabels(['{0}%'.format(value) for value in ticks])

    settings = {'standalone': True}
    settings.update(kwargs)

    return render(**settings)


def plot_local_hue_shifts(specification, x_ticker=False, **kwargs):
    """
    Plots the local hue shifts according to
    *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    specification : ColourQuality_Specification_ANSIIESTM3018
        *ANSI/IES TM-30-18 Colour Rendition Report* specification.
    x_ticker : bool, optional
        Whether to show the *X* axis ticker and the associated label.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> from colour import SDS_ILLUMINANTS
    >>> from colour.quality import colour_fidelity_index_ANSIIESTM3018
    >>> sd = SDS_ILLUMINANTS['FL2']
    >>> specification = colour_fidelity_index_ANSIIESTM3018(sd, True)
    >>> plot_local_hue_shifts(specification)
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    settings = kwargs.copy()
    settings['standalone'] = False

    _figure, axes = plot_16_bin_bars(specification.R_hs, '{0:.2f}', x_ticker,
                                     **settings)
    axes.set_ylim(-0.5, 0.5)
    axes.set_yticks(np.arange(-0.5, 0.51, 0.1))
    axes.set_ylabel('Local Hue Shift ($R_{hs,hj}$)')

    settings = {'standalone': True}
    settings.update(kwargs)

    return render(**settings)


def plot_local_colour_fidelities(specification, x_ticker=False, **kwargs):
    """
    Plots the local colour fidelities according to
    *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    specification : ColourQuality_Specification_ANSIIESTM3018
        *ANSI/IES TM-30-18 Colour Rendition Report* specification.
    x_ticker : bool, optional
        Whether to show the *X* axis ticker and the associated label.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> from colour import SDS_ILLUMINANTS
    >>> from colour.quality import colour_fidelity_index_ANSIIESTM3018
    >>> sd = SDS_ILLUMINANTS['FL2']
    >>> specification = colour_fidelity_index_ANSIIESTM3018(sd, True)
    >>> plot_local_colour_fidelities(specification)
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    settings = kwargs.copy()
    settings['standalone'] = False

    _figure, axes = plot_16_bin_bars(specification.R_fs, '{0:.0f}', x_ticker,
                                     'Horizontal', **settings)
    axes.set_ylim(0, 100)
    axes.set_yticks(np.arange(0, 101, 10))
    axes.set_ylabel('Local Color Fidelity ($R_{f,hj}$)')

    settings = {'standalone': True}
    settings.update(kwargs)

    return render(**settings)


def plot_colour_fidelity_indexes(specification, **kwargs):
    """
    Plots the local chroma shifts according to
    *ANSI/IES TM-30-18 Colour Rendition Report*.

    Parameters
    ----------
    specification : ColourQuality_Specification_ANSIIESTM3018
        *ANSI/IES TM-30-18 Colour Rendition Report* specification.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes

    Examples
    --------
    >>> from colour import SDS_ILLUMINANTS
    >>> from colour.quality import colour_fidelity_index_ANSIIESTM3018
    >>> sd = SDS_ILLUMINANTS['FL2']
    >>> specification = colour_fidelity_index_ANSIIESTM3018(sd, True)
    >>> plot_colour_fidelity_indexes(specification)
    ... # doctest: +ELLIPSIS
    (<Figure size ... with 1 Axes>, <...AxesSubplot...>)
    """

    _figure, axes = artist(**kwargs)

    bar_count = len(_TCS_BAR_COLOURS)
    axes.bar(
        np.arange(bar_count) + 1,
        specification.R_s,
        color=_TCS_BAR_COLOURS,
        width=1,
        edgecolor='black',
        linewidth=CONSTANTS_COLOUR_STYLE.geometry.short / 3)
    axes.set_xlim(0.5, bar_count + 0.5)
    axes.set_ylim(0, 100)
    axes.set_yticks(np.arange(0, 110, 10))
    axes.set_ylabel('Color Sample Fidelity ($R_{f,CESi}$)')

    ticks = list(range(1, bar_count + 1, 1))
    axes.set_xticks(ticks)

    labels = [
        'CES{0:02d}'.format(i) if i % 3 == 1 else ''
        for i in range(1, bar_count + 1)
    ]
    axes.set_xticklabels(labels, rotation=90)

    return render(**kwargs)
