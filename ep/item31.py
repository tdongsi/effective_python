# Stupid version of Insertion Sort for performance profiling

from bisect import bisect_left
from random import randint
from cProfile import Profile
from pstats import Stats

def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]

profiler = Profile()
# profiler.runcall(insertion_sort, data)
profiler.runcall(lambda: insertion_sort(data))

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
stats.print_callers()
