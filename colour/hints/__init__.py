# -*- coding: utf-8 -*-
"""
Annotation Type Hints
=====================

Defines the annotation type hints, the module exposes many aliases from
:mod:`typing` and :mod:`numpy.typing` to avoid having to handle multiple
imports.
"""

from __future__ import annotations

import numpy as np
import re
from numpy.typing import ArrayLike
from types import ModuleType
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Iterable,
    Iterator,
    List,
    Mapping,
    NewType,
    Optional,
    Union,
    Sequence,
    TextIO,
    Tuple,
    TYPE_CHECKING,
    Type,
    TypeVar,
)
try:
    from typing import Literal, Protocol  # type: ignore[misc]
except ImportError:
    from typing_extensions import Literal, Protocol  # type: ignore[misc]

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'Any',
    'Callable',
    'Dict',
    'Generator',
    'Iterable',
    'Iterator',
    'List',
    'Mapping',
    'ModuleType',
    'Optional',
    'Union',
    'Sequence',
    'TextIO',
    'Tuple',
    'Type',
    'RegexFlag',
    'DTypeBool',
    'DTypeInteger',
    'DTypeFloating',
    'DType',
    'Boolean',
    'Integer',
    'Floating',
    'Number',
    'Literal',
    'Dataclass',
    'ArrayLike',
    'IntegerOrArrayLike',
    'FloatingOrArrayLike',
    'ScalarType',
    'NDArray',
    'IntegerOrNDArray',
    'FloatingOrNDArray',
    'TypeInterpolator',
    'TypeExtrapolator',
    'array_like_to_floating_or_ndarray_1',
    'array_like_to_floating_or_ndarray_2',
    'multiply_ndarray_with_floating',
    'multiply_ndarray_with_floating_or_ndarray',
]

Any = Any
Callable = Callable
Dict = Dict
Generator = Generator
Iterable = Iterable
Iterator = Iterator
List = List
Mapping = Mapping
ModuleType = ModuleType
Optional = Optional
Union = Union
Sequence = Sequence
TextIO = TextIO
Tuple = Tuple
Type = Type

RegexFlag = NewType('RegexFlag', re.RegexFlag)

DTypeBool = np.bool_

DTypeInteger = Union[np.int8, np.int16, np.int32, np.int64, np.uint8,
                     np.uint16, np.uint32, np.uint64]

DTypeFloating = Union[np.float16, np.float32, np.float64]

DType = Union[DTypeInteger, DTypeFloating]

Boolean = Union[bool, DTypeBool]

Integer = Union[int, DTypeInteger]
Floating = Union[float, DTypeFloating]

Number = Union[Integer, Floating]

# TODO: Use "typing.Literal" when minimal Python version is raised to 3.8.
Literal = Literal

# TODO: Revisit when "Mypy" 0.920 is released and use Protocol
Dataclass = Any

ArrayLike = ArrayLike

IntegerOrArrayLike = Union[Integer, ArrayLike]
FloatingOrArrayLike = Union[Floating, ArrayLike]

ScalarType = TypeVar('ScalarType', bound=np.generic, covariant=True)

# TODO: Use "numpy.typing.NDArray" when minimal Numpy version is raised to
# 1.21.
if TYPE_CHECKING:
    NDArray = np.ndarray[Any, np.dtype[ScalarType]]
else:
    NDArray = np.ndarray

IntegerOrNDArray = Union[Integer, NDArray]
FloatingOrNDArray = Union[Floating, NDArray]


class TypeInterpolator(Protocol):
    x: NDArray
    y: NDArray

    def __init__(self, *args: Any, **kwargs: Any):
        ...

    def __call__(self, x: FloatingOrArrayLike) -> FloatingOrNDArray:
        ...


class TypeExtrapolator(Protocol):
    interpolator: TypeInterpolator

    def __init__(self, *args: Any, **kwargs: Any):
        ...

    def __call__(self, x: FloatingOrArrayLike) -> FloatingOrNDArray:
        ...


def array_like_to_floating_or_ndarray_1(
        a: Union[ArrayLike, List[FloatingOrNDArray]]) -> FloatingOrNDArray:
    return np.array(a)


def array_like_to_floating_or_ndarray_2(
        a: Union[ArrayLike, List[FloatingOrNDArray]]) -> FloatingOrNDArray:

    b = array_like_to_floating_or_ndarray_1(a)

    return array_like_to_floating_or_ndarray_1([b, b, b])


def multiply_ndarray_with_floating(a: NDArray, b: Floating) -> NDArray:
    return a * b


def multiply_ndarray_with_floating_or_ndarray(a: NDArray,
                                              b: FloatingOrNDArray) -> NDArray:
    return a * b
