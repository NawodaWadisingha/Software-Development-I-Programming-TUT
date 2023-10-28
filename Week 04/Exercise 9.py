while True:
    print("""Menu Options:\n1. Option 1\n2. Option 2\n3. Option 3\n4. Quit\n""")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("You selected Option 1\n")
        elif choice == 2:
            print("You selected Option 2\n")
        elif choice == 3:
            print("You selected Option 3\n")
        elif choice == 4:
            print("Goodbye!\n")
            break  
        else:
            print("Option is not recognised\n")

    except ValueError:
        print("Enter an Integer\n")