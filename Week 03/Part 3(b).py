user_input = input("Enter the calculation you want to solve according to followig example\nexample:3 + 2: \n")
x = user_input.split()
if len(x)!= 3:
    print("Invalid user input")
else:
    num1 = x[0]
    operator = x[1]
    num2 = x[2]
    num1 = int(num1)
    num2 = int(num2)


    try:
        match operator:
            case "+":
                print("answer is:" ,num1 + num2) 
            case "-":
                print("answer is:" ,num1 - num2)
            case "*":
                print("answer is:" ,num1 * num2)  
            case "/":
                print("answer is:" ,num1 / num2)
            case _:
                print("Invalid option Entered")
    except ZeroDivisionError:
        print("Error")