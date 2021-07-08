string = "Python for Beginners"

print(len(string))  # length of string

print(string.upper())  # does NOT modify original, creates new string
print(string.lower())  # does NOT modify original, creates new string

print(string.find("B"))  # returns index of first occurrence of that character
print(string.find("gin"))  # returns index of first occurrence of that character

print(string.replace("Beginners", "Dummies"))  # replaces word/alphabet
print(string.replace("o", "a"))

# check existence of character / sequence of characters in a String
# "in" operator produces a BOOLEAN value, "find()" method returns the index
print("Beginners" in string)
