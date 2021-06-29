secret_number = 7
guess_count = 1
guess_limit = 3

while guess_count <= guess_limit:
    guess_number = int(input("Guess a number from 1 to 9 : "))
    guess_count += 1
    if guess_number == secret_number:
        print("YOU WON !!!")
        break
else:  # python can have else block in while loops
    print("YOU LOST !!!")

