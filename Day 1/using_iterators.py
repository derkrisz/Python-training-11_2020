l = [n for n in range(10,0,-1)] # a generator
t = (n for n in range(20,10,-1)) # generate a tuple

for item in l:
    print(item)

for thing in t:
    print(thing)

# dictionary object: a collection of name-value pairs
# pairs are not in order

acuse = {'room':'hall', 'weapon':'lead pipe', 'person': 'rev green'}
acuse['version'] = 'classic'
acuse['room'] = 'library'

#iterate over dict
for card in acuse:
    print(card, acuse[card])

for key, value in acuse.items():
    print(key, value)

# using sets
# a set can only contain unique values
s = set((3,2,1,2,6,7,3))
print(s)
s2 = {*l, t, True, 'also'} # uniqueness is ALWAYS basd on VALUE
print (*s2) # the asterix unpacks the collection

# a set is very useful for removing duplicate values from a collection