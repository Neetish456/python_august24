#probelem statement: Read  a number from the user and check if the number is an even number or not  
    #To read datat from the console , we can use input(). however the input() alwats read only a string as usual with all other
        # mentioned within quotes is a string literal

print("App that checks if the given number is an Even number or Not!")
my_number = int(input("Enter a number : "))

if my_number %2 == 0:
    print(my_number,"   is an Even Number.")
else:
    print(my_number," is not an Even Number.")