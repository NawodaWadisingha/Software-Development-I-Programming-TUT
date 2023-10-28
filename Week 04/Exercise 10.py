import random 
count=0
hidden =random.randint(1,20)

while (count<5):
    try:
        guess = int(input("Enter your guess: "))
        count += 1

        if guess != hidden:
            print (guess, "is not correct")

            if guess>hidden:
                print("The value is higher than the hidden value\n")

            else:
                print("The value is lower than the hidden value\n")

        else:
            print (guess, "is correct")
            break
        
    except ValueError:
        print("Enter an integer")