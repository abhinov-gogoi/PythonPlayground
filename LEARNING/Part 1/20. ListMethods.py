numbers = [4, 65, 1, 82, 3, 4, 4, 7, 2, 98]
print(numbers)

# Add to last
numbers.append(23)
print(numbers)

# Insert at specific index
numbers.insert(0, 100)
print(numbers)

# Remove an item
numbers.remove(65)
print(numbers)

# Remove at end of list
numbers.pop()
print(numbers)

# Return index of a number
print(numbers.index(82))
# print(numbers.index(1000))

# Check existence within a list, (returns a Boolean)
print(82 in numbers)
print(1000 in numbers)

# Count frequency of an element
print(numbers.count(4))

# Sorting a list
numbers.sort()
print(numbers)

# Reversing a list
numbers.reverse()
print(numbers)

# Copy a list to another list
numbers2 = numbers.copy()
print(numbers2)

# Clearing a list
numbers.clear()
print(numbers)
