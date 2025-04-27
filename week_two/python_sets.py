set_one = set()
set_two = set()
set_three = set()

# Add elements to set_one
print("Enter set one elements (5 unique numbers):")
while len(set_one) < 5:
    number = int(input("Enter a number: "))
    set_one.add(number)
    
print("Enter set two elements (5 unique numbers):")  
while len(set_two) < 5:
    number = int(input("Enter a number: "))
    set_two.add(number)

set_three = set_one.intersection(set_two)
print("Set one:", set_one) 
print("Set two:", set_two)
print("Set three:", set_three)

# set_one = set()
# set_two = set()

# # Add elements to set_one
# while len(set_one) < 5:
#     try:
#         number = int(input("Enter a number for set_one: "))
#         set_one.add(number)
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# print("Set One:", set_one)
    
    
        


