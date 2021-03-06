from timer.timer import timeit

@timeit
def fib(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

fib(10)
fib(11)
fib(15)
fib(17)
