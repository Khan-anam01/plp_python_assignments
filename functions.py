def main():
    x = get_int()
    print (f"x is {x}")

def get_int():   
    while True:
        try:
            x = int(input ("what is x: "))
            # return int(input ("what is x: "))
            # return x - can be used to break the loop 
        except ValueError: # catches the ValueError
            print ("x is not an integer!!")
            # pass - skips the need to output anything
        else: # cathces the NameError 
            return x
        

main()