print("for loop in String")
for items in "Python":
    print(items)

print("for loop in List of Numbers")
for items in [1, 2, 3, 4, 5, 6]:
    print(items)

print("for loop in List of Strings")
for name in ["Abhi", "Amit", "Adii", "Alex"]:
    print(name)

print("for loop in Mixed List ")
for name in ["Dog", True, 467, 99.99, 'qwerty']:
    print(name)

print("for loop in range of numbers")
for i in range(10):
    print(i)

print("for loop between range of numbers")
for i in range(50, 60):
    print(i)

print("for loop between range of numbers with SKIP value")
for i in range(70, 90, 3):
    print(i)

# For print in same line
for name in ["Abhi", "Amit", "Adii", "Alex"]:
    print(name, end=" ")
