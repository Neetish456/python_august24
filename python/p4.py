#problem statement: Accept 3 distinct numbers and find smallest among them 
number1 = int(input('Enter the first number : '))
number2 = int(input('Enter the second number : '))
number3 = int(input('Enter the third number : '))

if (number1 < number2 and number1 < number3):
    print(number1," is the smallest number among the three.")
elif ( number2 < number3):
    print(number2," is the smallest number among the three.")
else:
    print(number3," is the smallest number among the three.")

print("Using built-in functions : ", min(number1,number2, number3) , " is the smallest number among the three.")
