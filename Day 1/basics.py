print('Python')
# username = input('enter your username')

# numbers
a = 2.0
b = 7
c = 3

#print(a+b)
#print(c/b)
#print(a**b)
#print(b/a, b//a, b%a)

# types
#print(type(a), type('hello'))

i = None
b = True # or False
#print (type(i), type(b))

# immutable strings
coffee = 'black with no sugar'
print(coffee[0:7:2]) #[start:stop-before:step]
print(coffee[::-1])

# logical conditions
if a < 0: # colon indicates start of a block
    print('negative value')
elif a < 100: 
    print('under 100')
else:
    print('100 or more')

# -1 for clue, -2 to quit

g = int(input('enter a number '))
# we can use and or and ! (not) in logic
if g == -1:
    print('clue...')
elif g == -2:
    print('game over')

# iterators 
while g != 0:
    print(g)
    g -= 1
    if g < -3:
        break

for i in range(0,10,3):
    print(i)

print(i)

r = range(100,0,-1)
for i in r:
    print(i)