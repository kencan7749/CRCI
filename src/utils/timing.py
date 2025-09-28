from time import perf_counter
from contextlib import contextmanager

@contextmanager
def timer():
    t0 = perf_counter()
    yield lambda: perf_counter() - t0
