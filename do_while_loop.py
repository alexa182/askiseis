secret_number = 7

while True:
    guess = int(input("guess a number between 1 and 10: "))

    if guess == secret_number:
        print("YOU GUEST IT")
        break

