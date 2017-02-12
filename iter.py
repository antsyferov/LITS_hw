class MyIterator(object):
    def __init__(self, arg):
        self.arg = arg
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.arg):
            a = self.arg[self.i]
            self.i += 1
            return a
        raise StopIteration()

if __name__ == '__main__':
    lst = [1, 2, 3]
    it = iter(MyIterator(lst))
    print(next(it))
    print(next(it))
    print(next(it))

        