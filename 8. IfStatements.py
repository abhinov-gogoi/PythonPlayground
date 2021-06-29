is_hot = False
is_cold = False

if is_hot:
    print("Its a hot day.")
    print("Drink Water !!")
elif is_cold:
    print("Its a cold day.")
    print("Wear warm clothes.")
else:
    print("Its a pleasant day.")

print("Enjoy your day.")

print("------------EXERCISE----------")
# Price of a house is $1 Million
# If the Buyer has good credit, they need to put down 10%
# Otherwise they need to put down 20%
# Print the down payment

price = 1_000_000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment = ${down_payment}")



