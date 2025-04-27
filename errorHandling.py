while True:
    try:
        x = int(input ("what is x: "))
    except ValueError: # catches the ValueError
        print ("x is not an integer!!")
    else: # cathces the NameError 
        break

print (f"x is {x}")

import sys

try:
    print(f"hello my name is {sys.argv[1]}")
except IndexError:
    pass