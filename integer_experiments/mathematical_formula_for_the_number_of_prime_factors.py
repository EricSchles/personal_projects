from multiprocessing import Process,Manager
import numpy as np
from collections import OrderedDict

#credit to: http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //=d
        d += 1
        if d*d > n:
            if n >1: factors.append(n)
            break
        
def processing(size,count):
    i = 0
    manager = Manager()
    dicter = manager.dict()
    while i < size:
        p = Process(target=prime_factors,args=(i,dicter,))
        p.start()
        if count % 100: p.join()
        i += 1
    return dicter

def main():
    x = []
    y = []
    count = 0
    for size in range(0,1000,5):
        dicter = processing(size,count)
        dicter = OrderedDict(dicter)
        listing = sorted(dicter.items(),key=lambda i:i[0])
        x.append([elem[0] for elem in listing])
        y.append([elem[1] for elem in listing])
        count += 1
    max_length = max([len(i) for i in x])
    for ind,val in enumerate(x):
        padding = max_length - len(val)
        for i in range(padding):
            val.append(0)
            y[ind].append(0)
    print(x,y)
if __name__ == '__main__':
    main()
