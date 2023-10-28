try:
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0 :
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number")
except:
    print(f"{num} is not a number")
