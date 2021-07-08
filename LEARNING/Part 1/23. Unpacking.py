# UNPACKING can be applied in LISTS and TUPLES

coordinates = (1, 2, 3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x, y, z)

# This can be achieved with less code using UNPACKING feature
x1, y1, z1 = coordinates
print(x1, y1, z1)

# Same can be applied in lists as well
