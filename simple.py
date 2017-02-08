from m import pow
from functools import reduce
import operator

if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    print(reduce(operator.add, lst, 100))
