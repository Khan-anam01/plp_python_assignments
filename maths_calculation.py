choice = "YES"
while choice == "YES":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operand = input("Enter the operand(*, /, +, -, %): ")
        result = 0
    except ValueError:
        print("Invalid input!")
        break

    if (operand == "*"):
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif (operand == "/"):
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("a number can be divised by 0")
    elif (operand == "+"):
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif (operand == "-"):
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif (operand == "%"):
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("a number can be divised by 0")
    else:
        print("Invalid operand!")
    
    choice = input("Do you want to do another calculation?(yes/no): ").upper()

