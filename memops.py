"""
Defines the basic classes used to facilitate the functionality of the sorting algorithms.


"""

from time import perf_counter


class Read:

    def __init__(self):
        self.reads = 0
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
        self.write_time = 0

    def update(self, ls, pos, val):
        stamp = perf_counter()
        ls[pos] = val
        self.write_time += perf_counter() - stamp
        self.writes += 1

    def swap(self, ls, a, b):
        stamp = perf_counter()
        ls[a], ls[b] = ls[b], ls[a]
        self.write_time += perf_counter() - stamp
        self.writes += 2

    def reset(self):
        self.writes = 0
        self.write_time = 0
