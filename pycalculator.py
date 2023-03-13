# (03/12/2023)

creator = 'cade collison'

while True:
    print(f"Welcome to {creator.title()}'s calculcator!\n")
    start = input("Enter 'start' to begin!\n\n\t~ ").lower()
    if start == 'start':
        print("\nWelcome in, let's get cracka-lackin'!")
        break
    else:
        print("\nMaybe next time! ;)\n")
        False

while start == 'start':
    value_1 = input("\nEnter value one:\n\n\t~ ")
    if value_1[not 1].isnumeric():
        print(f"\n{value_1}\n")
        value_1[not 1].isnumeric() == True
    elif operator[0] == 'c':
            break
    else:
        print("\nOopsie-dasiey! Looks like you didn't enter a number.")
        redemption = input("\tWould you like to try again? (yes/no)\n\n\t~ ")
        if redemption == 'yes':
            break
        else:
            print("\nRun the code to activate calculator.")
            quit()


    def add(value_1, value_2):
        sum = float(value_1) + float(value_2)
        print(f"\nAnswer = {sum}")

    def subtract(value_1, value_2):
        sum = float(value_1) - float(value_2)
        print(f"\nAnswer = {sum}")
        
    def multiply(value_1, value_2):
        sum = float(value_1) * float(value_2)
        print(f"\nAnswer = {sum}")
            
    def divide(value_1, value_2):
        sum = float(value_1) / float(value_2)
        print(f"\nAnswer = {sum}")



    while value_1[not 1].isnumeric() == True:
        operator = input(f"Choose an operator!\n\n(+, -, *, or /)\n\n\t~ {value_1} ")
        operator_options = ['+', '-', '*', '/']
        operator_err_msg = f"{operator} is not a valid operator."
        if operator[0] == '+':
            print(f"\nEnter value two:")
            value_2 = input(f"\n\t{value_1} + ")
            if value_2[not 1].isnumeric():
                add(value_1, value_2)
                break
            else: 
                print("Looks like we need to enter a number.")
        elif operator[0] == 'c':
            break
        else:
            print(operator_err_msg)
            break
    
        if operator[0] == '-':
            print(f"\nEnter value two:")
            value_2 = input(f"\n\t{value_1} - ")
            if value_2[not 1].isnumeric():
                subtract(value_1, value_2)
                break
            else: 
                print("Looks like we need to enter a number.")
        elif operator[0] == 'c':
            break
        else:
            print(operator_err_msg)
            break
            
        if operator[0] == '*':
            print(f"\nEnter value two:")
            value_2 = input(f"\n\t{value_1} * ")
            if value_2[not 1].isnumeric():
                multiply(value_1, value_2)
                break
            else: 
                print("Looks like we need to enter a number.")
        elif operator[0] == 'c':
            break
        else:
            print(operator_err_msg)
            break
                
        if operator[0] == '/':
            print(f"\nEnter value two:")
            value_2 = input(f"\n\t{value_1} / ")
            if value_2[not 1].isnumeric():
                divide(value_1, value_2)
                break
            else: 
                print("Looks like we need to enter a number.")
        elif operator[0] == 'c':
            break
        else:
            print(operator_err_msg)
            break