#problem statement: Write a Program to reverse a given number.

inputnum1 = int(input("Enter the number to find the reverse a given number: "))
number = inputnum1
reverse = 0
while number >= 0:
    remainder = number%10
    reverse = (reverse*10) + remainder
    number = number//10
    
print("the Sum of even digits in given number is  : ", reverse)