def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    import time
    start = time.time()
    print(fib(40))
    end = time.time()
    print(end - start)