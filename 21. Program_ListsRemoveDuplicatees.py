# Write a program to remove duplicates from a list

numbers = [1, 4, 2, 7, 3, 7, 8, 9, 2, 5, 4, 1, 2, 3, 2, 1, 4, 5, 7, 8, 9, 0]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)

uniques.sort()
print(uniques)
