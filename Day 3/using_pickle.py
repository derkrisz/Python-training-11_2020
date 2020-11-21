import pickle, datetime 

# serialize some complex structures
now = datetime.datetime.utcnow()
print(now)
pickled = pickle.dumps(now)
print(pickled)

class Tiny:
    def __init__(self):
        pass
    def __str__(self):
        return 'This is the tiny class'

t = Tiny()
pickled_t = pickle.dumps(t)
print(pickled_t)

# deserialize
retrieved = pickle.loads(pickled_t)
print(retrieved)

then = pickle.loads(pickled)
print(then)