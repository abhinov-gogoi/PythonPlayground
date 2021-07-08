# Write a program to find largest number in a list

numbers = [45, 22, 74, 101, 47, 8, 42, 75, 12, 78]

largest_no = numbers[0]

for num in numbers:
    if num > largest_no:
        largest_no = num

print(largest_no)

