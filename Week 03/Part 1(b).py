age = input("Please enter your age: \n")
try:
    age = int(age)
    if age>=18:
        print("Can Vote")
except:
    print("Invalid Credintials")