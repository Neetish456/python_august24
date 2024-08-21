#problem statement: Program to Find the Largest Digit in a given number.

inputnum1 = input("Enter the number to find the largest Digit of a number : ")
largest = inputnum1[0]
for i in inputnum1:
    if i > largest:
        largest = i
    else:
        continue
print("the largest digit in the given number is  : ", largest)

#smallest

inputnum1 = input("Enter the number to find the smallest Digit of a number : ")
smallest = inputnum1[0]
for i in inputnum1:
    if i < smallest:
        smallest = i
    else:
        continue
print("the largest digit in the given number is  : ", smallest)
    


