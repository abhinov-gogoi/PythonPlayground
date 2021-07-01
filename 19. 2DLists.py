# 2D Lists -> Lists inside lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing matrix elements
print(matrix)
print(matrix[0][0])
print(matrix[1][1])

# Changing values in 2D lists
matrix[1][1] = 345
print(matrix)

# Accessing matrix elements using nested loops
for row in matrix:
    for item in row:
        print(item)


