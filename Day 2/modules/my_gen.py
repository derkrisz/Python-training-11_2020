def gen_squares(min=0, max=10, step=1): # we supply defaults here
    n = min
    while n <= max:
        yield n*n
        n += step

if __name__ == '__main__':
    result = gen_squares(1, 10)
    print(type(result))

    for sq in result:
        print(sq)