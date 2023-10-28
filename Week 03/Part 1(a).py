n = input("Give me a number over 100: ")
try:
    n = int(n)
    if n<=100:
        print(n,"is not over 100")
except ValueError:
    print(n,"is not a number")