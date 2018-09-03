a = range(10)
# squares = [x**2 for x in a]
squares = map(lambda x: x**2, a)
print(squares)

b = range(5)
# Recommended
squares = [x**2 for x in b if x % 2 == 0]
print(squares)
# Old way
squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, b))
print(squares)

