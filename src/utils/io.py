# Fast I/O helpers for CP
import sys
data = sys.stdin.buffer.read().split()
it = iter(data)

def next_token():
    return next(it)

def ni():
    return int(next_token())

def nf():
    return float(next_token())

def ns():
    return next_token().decode()
