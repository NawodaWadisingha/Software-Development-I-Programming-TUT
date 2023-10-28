total = 0
count = 0
score = int(input("Enter score, (Enter -9 to end):\n"))
while count == 0 and score == -9:
   print("Before ending the programme ensure that at least one score has been entered")
   score = int(input("Enter score, (Enter -9 to end):\n"))

while True:
    if score != -9:
        total = total + score
        count = count + 1 
        score = int(input("Enter score, (Enter -9 to end):\n"))
    else:
        break
average = float(total)/count
print("Average of score entered is", average)