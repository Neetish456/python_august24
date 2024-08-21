#problem statement: Progra to find the sum of Digists of a number.

inputnum1 = int(input("Enter the number to find the sum of Digits : "))

sum1 = 0
for i in range(0,inputnum1+1):
    sum1 = sum1 + i
print("The sum of Digits of the given number is : ",sum1)

