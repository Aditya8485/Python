p = r'd:/vs code/claude code/INHERITANCE/chef.py'
with open(p,'rb') as f:
    b = f.read()
print('bytes:', b)
print('\nlines repr:')
for i, line in enumerate(b.splitlines(), 1):
    print(i, repr(line))
print('\nclass line ords:')
for i, line in enumerate(b.splitlines(), 1):
    if b'class' in line:
        print(i, [ord(c) for c in line])
        break
