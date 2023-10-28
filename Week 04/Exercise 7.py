import random
same = 0

for i in range(101):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    if dice_1 == dice_2:
        same = same+1
    else:
        continue
print(f"Out of 100 you rolled {same} doubles.")