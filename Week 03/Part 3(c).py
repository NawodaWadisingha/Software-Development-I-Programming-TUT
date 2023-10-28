meal_cost = int(input("Enter the cost of the meal: "))
print("ratings:\n1 = Totally satisfied\n2 = Satisfied\n3 = Dissatisfied")
satisfaction = int((input("Enter satisfaction level: ")))
if satisfaction == 1:
    tip = (meal_cost*20)/100
    print(f"Satisfaction level is {satisfaction} and your tip is {tip}")
elif satisfaction == 2:
    tip = (meal_cost*15)/100
    print(f"Satisfaction level is {satisfaction} and your tip is {tip}")
elif satisfaction == 3:
    tip = (meal_cost*10)/100
    print(f"Satisfaction level is {satisfaction} and your tip is {tip}")
else:
    print("Please eter Valid inputs")