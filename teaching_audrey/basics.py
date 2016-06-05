x = 0
print(type(x))
x = "hello"
print(type(x))
class Hello:
    def __init__(self):
        self.data = 0

x = Hello()
print(type(x))
def func():
    return "hello"
x = func
print(type(x))
def func2(f,x):
    return 2*f(x)
print(func2(lambda x:x*x,2))
