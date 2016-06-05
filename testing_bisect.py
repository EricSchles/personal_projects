import bisect
from time import time

thing = range(100)
thing.append(101)
stuff = thing[:]

start_insort = time()
bisect.insort(thing,100)
print time() - start_insort,"timing bisect"

start_append_sort = time()
stuff.append(100)
stuff.sort()
print time() - start_append_sort,"timing apending then sorting"


