hidden = 6
while True:
    guess = int(input("Enter a guess number between 1 an 20: "))
    if hidden != guess:
        print(f"{guess} is not correct")
    else:
        print(f"{guess} was correct")
        break