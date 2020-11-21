
# params: positional, default (keyword), or *args lastly *kwargs

def do_stuff(a, b=2, *args, **kwargs):
    for item in args:
        print(item)
    for member in kwargs:
        print(f'{member} {kwargs[member]}')
    return a**b

if __name__ == '__main__':

    print(do_stuff(2, 3, True, 42, 'hello', n=42, user='Othello'))
   