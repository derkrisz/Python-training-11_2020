# lists
l = [9,8,7,6]
for n in l:
    print(n)

e = l
e.append(9)

print(l)

print(l[3], l[:5], l[::-1])

# tuples
my_t = (6,5,4,3)
for t in my_t:
    print(t)

#careful
my_tuple = (3,) #this IS a tuple

y = tuple(l)
print(y)
l.append('lunch')
print(y,l) # the tuple is created by VALUES i.e not by reference to l

# multi-dimensions (collections within collections) and non-existent members
l1 = [True, False, None]
l2 = ['Peter', 'flopsy', 'cottontail']
l3 = [(6,5,4), 'text', 3.21, [],]
collect = [l1, l2, l3]

print(collect[0][1])
print(collect[2][0][1])
print(collect[1][1][5])