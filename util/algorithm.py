from . import memops


class SortingAlgorithm:
    dispatch = dict()

    def __init__(self, name, key):
        self.runtime = []
        self.reads = []
        self.writes = []
        self.name = name

        self.reader = memops.Read()
        self.writer = memops.Write()

        if not key:
            key = name[0:3] + "srt"
        SortingAlgorithm.dispatch[key] = self

    def _sort(self):
        pass

    def call(self, *args, **kwargs):
        self._sort(*args, **kwargs)
        self.runtime.append(self.reader.read_time + self.writer.write_time)
        self.reads.append(self.reader.reads)
        self.writes.append(self.writer.writes)
        self.reader.reset()
        self.writer.reset()

    def stats(self):
        print(f"Reads: {self.reads}\tWrites:{self.writes}")