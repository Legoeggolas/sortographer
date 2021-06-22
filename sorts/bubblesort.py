from util.algorithm import SortingAlgorithm

# to cythonize


class BubbleSort(SortingAlgorithm):

    def __init__(self, name, key=""):
        super().__init__(name, key)

    def _sort(self, ls):
        for i in range(len(ls) - 1):
            for j in range(len(ls) - i - 1):
                if self.reader.compare(ls[j], ls[j + 1]) == 1:
                    self.writer.swap(ls, j, j + 1)


class OptBubbleSort(SortingAlgorithm):

    def __init__(self, name, key=""):
        super().__init__(name, key)

    def _sort(self, ls):
        for i in range(len(ls) - 1):
            is_sorted = True
            for j in range(len(ls) - i - 1):
                if self.reader.compare(ls[j], ls[j + 1]) == 1:
                    self.writer.swap(ls, j, j + 1)
                    is_sorted = False
            if is_sorted:
                break


class multidirectionalBubbleSort(SortingAlgorithm):

    def __init__(self, name, key=""):
        super().__init__(name, key)

    def _sort(self, ls):
        start = 0
        end = len(ls) - 1
        while True:
            is_sorted = True
            for i in range(start, end):
                if self.reader.compare(ls[i], ls[i + 1]) == 1:
                    self.writer.swap(ls, i, i + 1)
                    is_sorted = False

            if is_sorted:
                return

            end -= 1

            for i in reversed(range(start, end)):
                if self.reader.compare(ls[i], ls[i + 1]) == 1:
                    self.writer.swap(ls, i, i + 1)
                    is_sorted = False

            if is_sorted:
                return

            start += 1


bsort = BubbleSort("bubble sort")
optbsort = OptBubbleSort("optimized bubble sort", "optbubsrt")
mdirbsort = multidirectionalBubbleSort("multidirectional bubble sort",
                                       "mdbubsrt")
