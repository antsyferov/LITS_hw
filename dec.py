from functools import wraps

def mywraps(base_f):
    def dec(func):
        func.__name__ = base_f.__name__
        return func
    return dec


def decorator(func):

    @mywraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper

@decorator
def summ(a, b):
    return a + b

@decorator
def sub(a, b=None, *args, **kwargs):
    return a - b

class dec:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        res = self.func(*args)
        return res

@dec
def mul(a, b):
    return a*b




def d1(func):
    print('d1', func.__name__)
    def w1(*args):
        print('w1')
        return func(*args) 
    return w1 

def d2(func):
    print('d2', func.__name__)
    def w2(*args):
        print('w2')
        return func(*args)
    return w2  

@d1
@d2
def div(a, b):
    print('div')
    return a/b

print(div(1, 1))