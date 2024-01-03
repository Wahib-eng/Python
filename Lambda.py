# Define lambda functions for basic arithmetic operations
add = lambda n1, n2: n1 + n2
sub = lambda n1, n2: n1 - n2
mul = lambda n1, n2: n1 * n2
div = lambda n1, n2: n1 / n2

# Infinite loop for continuous calculations
while True:
    # User input to continue or exit the program
    exit_choice = int(input("Enter 1 to continue or 0 to exit: "))
    
    # Break out of the loop if the user chooses to exit
    if exit_choice == 0:
        break

    # User input for two digits and the operation to perform
    digit1 = float(input("Enter the 1. digit: "))
    digit2 = float(input("Enter the 2. digit: "))
    operation = input("Enter the operation * - + /: ")

    # Perform the selected operation based on user input
    if exit_choice == 1:
        if operation == '+':
            print(f"{digit1} + {digit2} = {add(digit1, digit2)}")
        elif operation == '-':
            print(f"{digit1} - {digit2} = {sub(digit1, digit2)}")
        elif operation == '*':
            print(f"{digit1} * {digit2} = {mul(digit1, digit2)}")
        elif operation == '/':
            # Check for division by zero before performing the operation
            if digit2 != 0:
                print(f"{digit1} / {digit2} = {div(digit1, digit2)}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation")
