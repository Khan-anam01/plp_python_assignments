

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



