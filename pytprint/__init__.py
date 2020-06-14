# thread-safe print module

# https://bramcohen.livejournal.com/70686.html
from threading import Lock
import sys

mylock = Lock()
p = print


def print(*a, **b):
    with mylock:
        p(*a, **b)
    # https://stackoverflow.com/a/367065
    sys.stdout.flush()
