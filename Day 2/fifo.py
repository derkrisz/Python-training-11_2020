fout = None
try:
    fout = open('snip.txt', 'wt') # w = write, a = append,  t = text, x = exclusive
    print('this is a snippet of text', file=fout)
    fout.close() 
except FileExistsError as err:
    print('Cannot write, file already exists ', err)

# we can write to a file in chunks, useful for long or time-based writing

long_string = 'the while... loop will automatically close any open files\nwhich saves us doing it'
try:
    with open('long.txt', 'xt') as fout:
        size = len(long_string)
        offset = 0
        chunk = 24 # how many characters to write at a time
        while offset <= size: #  a while loop will automatically close a file when done
            fout.write(long_string[offset:offset + chunk])
            offset += chunk
except FileExistsError as err:
    print('Cannot write, file already exists ', err)
finally:
    fout.close()

# reading back from a text file
fin = open('long.txt', 'rt')
received = fin.read()
fin.close()
print(received)

# working with binary data
bdata = bytes(range(0,256))
fout = open('binfile', 'wb')
fout.write(bdata)
fout.close()
fin = open('binfile', 'rb')
received = fin.read()
fin.close()
print(received)
print(received.decode('utf-8', 'ignore'))