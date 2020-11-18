# import stuff 
from modules.sanitize import make_numeric
# declare globals - try to avoid polluting the global namespace

# declare functions
def find_hypot(x, y):
    r = (x*x+y*y)**0.5
    return r

# immediate code
if __name__ == '__main__': # is this the main module executed?
    x = input('value of x ')
    y = input('value of y ')
    x = make_numeric(x)
    y = make_numeric(y)
    result = find_hypot(x, y)
    print(result)