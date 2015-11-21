from __future__ import absolute_import, division, print_function

import pandas
import os
from toolz import curry, concat
import pandas as pd
import numpy as np
from collections import Iterator, Iterable
from odo import into
from odo.chunks import chunks
from odo.backends.csv import CSV
from multipledispatch import MDNotImplementedError

from ..dispatch import dispatch
from ..expr import Expr, Head, ElemWise, Distinct, Symbol, Projection, Field
from ..expr.core import path
from ..utils import available_memory
from ..expr.split import split
from .core import compute
from ..expr.optimize import lean_projection
from .pmap import get_default_pmap


__all__ = ['optimize', 'pre_compute']


@dispatch(Expr, CSV)
def optimize(expr, _):
    return lean_projection(expr)  # This is handled in pre_compute


@dispatch(Expr, CSV)
def pre_compute(expr, data, comfortable_memory=None, chunksize=2**18, **kwargs):
    comfortable_memory = comfortable_memory or min(1e9, available_memory() / 4)

    kwargs = dict()

    # Chunk if the file is large
    if os.path.getsize(data.path) > comfortable_memory:
        kwargs['chunksize'] = chunksize
    else:
        chunksize = None

    # Insert projection into read_csv
    oexpr = optimize(expr, data)
    leaf = oexpr._leaves()[0]
    pth = list(path(oexpr, leaf))
    if len(pth) >= 2 and isinstance(pth[-2], (Projection, Field)):
        kwargs['usecols'] = pth[-2].fields

    if chunksize:
        return into(chunks(pd.DataFrame), data, dshape=leaf.dshape, **kwargs)
    else:
        return into(pd.DataFrame, data, dshape=leaf.dshape, **kwargs)


Cheap = Head, ElemWise, Distinct, Symbol


@dispatch(Head, CSV)
def pre_compute(expr, data, **kwargs):
    leaf = expr._leaves()[0]
    if all(isinstance(e, Cheap) for e in path(expr, leaf)):
        return into(Iterator, data, chunksize=10000, dshape=leaf.dshape)
    else:
        raise MDNotImplementedError()
