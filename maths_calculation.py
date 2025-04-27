<<<<<<< HEAD


# while True:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = 0
#     operand = input("Enter the operation to be conducted(+, -, *, /, %):")
   
#     if (operand == "+"):
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#         break
#     elif (operand == "-"):
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#         break
#     elif (operand == "*"):
#         result = num1 * num2
#         print(f"{num1} * {num2} = {result}")
#         break
#     elif (operand == "/"):
#         if num2 != 0:
#             result = num1 / num2
#             print(f"{num1} / {num2} = {result}")
#         break
#     elif (operand == "%"):
#         if num2 != 0:
#             result = num1 % num2
#             print(f"{num1} % {num2} = {result}")
#         break
#     else:
#         print("Invalid operation")
#         break
num1 = float(input("Enter first number: "))  # Ensure num1 is defined
num2 = float(input("Enter second number: "))  # Ensure num2 is defined
operand = input("Enter operation (+, -, *, /, %): ")  # Ensure operand is defined

while True:
    
    if operand == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        break
    elif operand == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        break
    elif operand == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        break
    elif operand == "/":
        if num2 != 0:  # Prevent division by zero
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
        break
    elif operand == "%":
        if num2 != 0:  # Prevent modulo by zero
            result = num1 % num2  # Corrected: Using modulo instead of addition
            print(f"{num1} % {num2} = {result}")
        else:
            print("Error: Modulo by zero is not allowed.")
        break
    else:
        print("Invalid operation")
        break


=======
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
>>>>>>> 28c04b7c40696ed9cc7f5864ae73626bc072a72e

