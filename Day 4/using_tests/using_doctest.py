# doctest makes use of the docstring
import doctest

def square_num(num):
    '''
    This function returns the square of numbers under ten.
    Or raises an exception.
    >>> square_num(2)
    4
    >>> square_num(-3)
    9
    >>> square_num(16)
    Traceback (most recent call last):
    ...
    ValueError: input too large
    '''
    if num > 10:
        raise ValueError('input too large')
    else:
        return num * num

def square_range(a, b):
    '''
    returns the square of every integer from a to b inclusive
    >>> square_range(1, 10) # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 4, ..., 100]
    '''
    answer = []
    for i in range(a, b + 1):
        answer.append(i * i)
    return answer

if __name__ == '__main__':
    doctest.testmod(verbose=True)