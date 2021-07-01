# (key, value) SYNTAX

# dictionary = {
#     "key1": "value",
#     "key2": "value",
#     "key3": True,
#     "key4": 5000
# }

customer = {
    "name": "Abhi",
    "age": 25,
    "isMale": True
}

# Accessing dictionary values
print(customer["name"])
print(customer["age"])
# print(customer["Waahao"]) #  gives error
print(customer.get("Waahaaoo"))
print(customer.get("Waahaaoo", "default value"))

# Updating dictionary values
customer["name"] = "Abhinov Gogoi"
print(customer)

# Add new key, value
customer["birthday"] = "18 Dec 1996"
print(customer)
