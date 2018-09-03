import random

with open('/tmp/my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('/tmp/my_file.txt')]
print(value)

better = (len(x) for x in open('/tmp/my_file.txt'))
roots = ((x, x**2) for x in better)
print(next(roots))
print(next(better))
print(next(roots))
