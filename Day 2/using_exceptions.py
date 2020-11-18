l = [1, 2, 3]

while True:
    value = input('which member? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(l[position])
    except IndexError as err:
        print(f'no such index {value}', err)
    except:
        print('oops')

if __name__ == '__main__':
    pass