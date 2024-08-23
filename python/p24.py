#problem statement: Wrie a program to Check if a number is Prime.
number1 = int(input("Enter a number to check if it is Prime:"))
if number1 in [2,3,5]:
    print(" the given number ",number1, " is a prime number.")
elif number1%2 != 0 and number1%3 != 0 and number1%5 != 0:
    print(" the given number ",number1, " is a prime number.")