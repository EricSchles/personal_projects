from multiprocessing import Process,Queue
from time import time
def processing(x,q):
    q.put(x*x)

def proc(x):
    return x*x

start = time()
q = Queue()
results = []
for i in range(1000):
    p = Process(target=processing,args=(i,q,))
    p.run()
    results.append(q.get())


print(time()-start,"multiprocessing run")

start = time()
res = []
for i in range(1000):
    res.append(proc(i))

print(time() - start, "linear run")

print("Hello there")

def thing(x):
    return repr(x*x)

print(type(thing(5)))

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return repr(self.data)

head = Node(0)
cur = head
cur.next = Node(1)
while cur:
    print(cur)
    cur = cur.next
