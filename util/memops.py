"""
Defines the basic classes used to facilitate the functionality of the sorting algorithms.


"""

from time import perf_counter


class Read:

    def __init__(self):
        self.reads = 0
        self.auxreads = 0
        self.read_time = 0

    def compare(self, a, b):
        stamp = perf_counter()
        if a > b:
            equality = 1
        elif a < b:
            equality = -1
        else:
            equality = 0
        self.read_time += perf_counter() - stamp
        self.reads += 1
        return equality

    def reset(self):
        self.reads = 0
        self.read_time = 0


class Write:

    def __init__(self):
        self.writes = 0
        self.auxwrites = 0
        self.write_time = 0

    def update(self, ls: list, pos: int, val: int, *, aux=False):
        stamp = perf_counter()
        ls[pos] = val
        self.write_time += perf_counter() - stamp
        self.writes += 1

    def swap(self, ls: list, posA: int, posB: int, *, aux=False):
        stamp = perf_counter()
        ls[posA], ls[posB] = ls[posB], ls[posA]
        self.write_time += perf_counter() - stamp
        self.writes += 2

    def reset(self):
        self.writes = 0
        self.write_time = 0
