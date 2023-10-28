total = 0
for i in range(0,5):
    num =  input("Enter a number: ")
    try:
        num = int(num)
        total += num
    except ValueError:
        print(f"{num} is not a number")
        break
print(f"Total of the numbers is {total}")