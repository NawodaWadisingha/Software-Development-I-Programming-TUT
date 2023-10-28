import random

while True:
    hidden = random.randint(1,20)
    guess = int(input("Enter a guess number between 1 an 20: "))
    if guess<=20:
        if hidden != guess:
            print(f"{guess} is not correct")
            print(hidden)
        else:
            print(f"{guess} was correct")
            break
    else:
        print("Try again")