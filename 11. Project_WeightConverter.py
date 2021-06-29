weight = int(input("Enter Weight: "))
unit = input("(L)bs or (K)g? ")

if unit.upper()[0] == "L":
    print("You are " + str(weight*0.45) + " kilos")
elif unit.upper()[0] == "K":
    print("You are " + str(weight*2.20) + " pounds")
else:
    print("Please enter L or K")
