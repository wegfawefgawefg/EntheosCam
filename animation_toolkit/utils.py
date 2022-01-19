from itertools import tee

import numpy as np

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def dict_filter(d, condition):
    return {k: v for k, v in d.items() if condition(k, v)}

def sigspace(start, end, n):
    return 1/(1 + 1.5**-np.linspace(-10, 10, n)) * (end - start) + start
