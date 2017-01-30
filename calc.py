
import random

class ArgError(Exception):
    pass

def summ(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgError('Invalid parameters')
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    assert b != 0, 'Second arg should not be zero'
    return a/b

def sub(a, b):
    return a -b 

def get_random():
    return random.randint(1, 3)

def mul_random(x):
    return x * get_random()


if __name__ == '__main__':
    x = int(input('enter x: '))
    y = int(input('enter y: '))

    res = summ(x, y)
    print(res)