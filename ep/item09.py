# 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [x for row in matrix for x in row]
print(flatten)

squared = [[x**2 for x in row] for row in matrix]
print(squared)

filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)

# 3D matrix
matrix_3d = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]
flatten = [x for sublist1 in matrix_3d
           for sublist2 in sublist1
           for x in sublist2]
print(flatten)

# Recommended way
flatten = []
for sublist1 in matrix_3d:
    for sublist2 in sublist1:
        flatten.extend(sublist2)
print(flatten)

