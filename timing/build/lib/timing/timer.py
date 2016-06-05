from functools import wraps
from time import time

def timeit(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        start = time()
        f(*args,**kwargs)
        end = time() - start
        return end
    return wrapper

