import numpy as np
from timer.timer import timeit

def nth_number(x):
    return np.prod(np.array([elem**elem for elem in xrange(1,x+1)]))
    
