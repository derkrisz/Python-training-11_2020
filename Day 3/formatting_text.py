# ways to format text

n = 42
f = 4.32
s = 'text'

result = '%d %f %s'%(n, f, s)

print(result)

# the new way

new_result = '{} {} {}'.format(n, f, s)
# new_result = '{2} {0} {1} {2}'.format(n, f, s)
# new_result = '{2:s} {0:d} {1:f} {2:s}'.format(n, f, s)
new_result = '{2:s} {0:d} {1:.1f} {2:s}'.format(n, f, s)

print(new_result)

# the newest way

newest_result = f'{n} {f} {s}'

print(newest_result)