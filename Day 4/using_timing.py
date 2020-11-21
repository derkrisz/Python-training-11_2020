import time
from timeit import default_timer

def fib(n):
    if n <= 1:
        return n
    else:
        return ( fib(n-1)+fib(n-2) )


if __name__ == '__main__':
    start = time.time()
    start2 = default_timer()
    print (fib(35))
    end = default_timer()
    end2 = time.time()
    print(f'it took {end-start} seconds.')