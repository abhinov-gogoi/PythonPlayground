prompt = "----------CAR GAME----------" \
         "\nstart -> to start the car " \
         "\nstop -> to stop the car " \
         "\nquit -> to quit the game " \
         "\nhelp -> to display this menu"
print(prompt)

started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started ...")
        else:
            started = True
            print("Car Started !!")
    elif command == "stop":
        if not started:
            print("Car is not started")
        else:
            started = False
            print("Car Stopped !!")
    elif command == "help":
        print(prompt)
    elif command == "quit":
        break
    else:
        print("I don't understand that ... ")

print("You quit !!")
