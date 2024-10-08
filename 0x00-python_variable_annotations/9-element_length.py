#!/usr/bin/env python3
"""Type-annotated element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of sequence and int"""
    return [(i, len(i)) for i in lst]
