print("Enter 1 if you want to convert from Celsius to Fahrenheit\nor enter 2 if you want to convert from Fahrenheit to Celsius")
num = int(input("Enter 1 or 2: "))
temp = input("Enter the temperature that you want to convert: ")
temp = int(temp)
match num:
    case 1:
        print("Temperature in Fahrenheit",(temp*1.8)+32)
    case 2:
        print("Temperature in Celsius",(temp-32)/1.8)
    case _:
        print("Invalid option entered")