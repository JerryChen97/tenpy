"""To be used in the `-m` argument of benchmark.py."""
# Copyright 2019 TeNPy Developers, GNU GPLv3

import numpy as np
import tenpy.linalg.np_conserved as npc

import tenpy.tools.optimization as optimization
import itertools as it

import tensordot_npc


def setup_benchmark(*args, **kwargs):
    a, b, axes = tensordot_npc.setup_benchmark(*args, **kwargs)
    axes_a, axes_b = axes
    non_axes_a = [i for i in range(a.rank) if i not in axes_a]
    non_axes_b = [i for i in range(b.rank) if i not in axes_b]
    return a, b, ((non_axes_a, axes_a), (axes_b, non_axes_b))


def benchmark(data):
    a, b, axes = data
    axes_a, axes_b = axes
    a.combine_legs(axes_a)
    b.combine_legs(axes_b)
