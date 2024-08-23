#problem statement: Program to Find the Largest Digit in a given number.

#Problem statement: Program to find the second smallest digit in a number

inputnum1 = input("Enter the number to Find the 2nd smallest digit:")
digits = [] 

length = len(inputnum1)

for i in inputnum1:
    digits.append(i)
smallest = min(digits)

for i in range(1,length):
    smallest_2 = inputnum1[i-1]
    if  smallest > inputnum1[i]:
        smallest_2 = inputnum1[i]
        
print("The 2nd smallest digits in",inputnum1,"is",smallest_2)
