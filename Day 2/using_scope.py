# global scope
meta = 'this variable has a global scope'

def method():
    global meta # access the global-scoped meta from the local scope
    meta = 'this variable has a local scope'
    return meta


print(meta)
print(method())
print(meta)