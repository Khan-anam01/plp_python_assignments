numbers = []

while True:
    number = input("Enter a number or type 'end' to finish: ")
    
    if number.lower() == 'end':  # Check before conversion
        break
    
    try:
        numbers.append(int(number))
    except ValueError:
        print("Please enter a valid number.")

print("Numbers entered:", numbers)
print("Sum:", sum(numbers))