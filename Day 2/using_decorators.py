# declare decorator function (write a function and apply that functionality to other functions)
def square_int(func): #we expect a function as the only argument
    def do_stuff(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return do_stuff


def document_it(func):
    def inner(*args, **kwargs):
        print(f'The running function is called {func.__name__}')
        print(f'The docstring is {func.__doc__}')
        print(f'The positional arguments are {args}')
        print(f'The keyword arguments are {kwargs}')
        result = func(*args, **kwargs)
        print(f'The result of executing the function is {result}')
    return inner

# declare normal function
@document_it
@square_int
def add_ints(a, b):
    return int(a + b)

if __name__ == '__main__':
    print(add_ints(5, 3.8))