# declare re-usable functions

def make_numeric(value):
    # if type(value) == int or type(value) == float:
   # if isinstance(value, (int, float)):
   #     return value
   # else:
   #     return float(value)
    return value if isinstance(value, (int, float)) else float(value)


def ethel(*args): # using arguments
    # explore the positional arguments that may have been passed in
    if len(args) > 0:
        print(args)
    else:
        print('no positional arguments')

def einid(**kwargs): # using keyword arguments
    # explore the keyword arguments passed in
    print(kwargs)

def albert(*args, **kwargs): # * unpacks collection, ** unpacks key-value pairs
    if len(args) > 0:
        for item in args:
            print(type(item), item)
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            print(type(key), type(value), key, value)

# we can exercise the functions to check they work as expected
if __name__ == '__main__':
    test_values = (1, 2, 3.5, '5')
    a, b, c, d = test_values # this unpacks the tuple into the variables

    print(make_numeric(a), make_numeric(b), make_numeric(c), make_numeric(d))

    ethel()
    ethel(3, 4, True, einid)
    einid(x = 1, y = 3, f = ethel)
    albert(6, 7, 8, 'coffee', value = 9.0, geo = (-0.2, 52))