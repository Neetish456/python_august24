#problem statement: Program to Find count of digits of a number.

inputnum1 = int(input("Enter the number to find the count of Digits of a number : "))
stringconversion = str(inputnum1)

for i in range(0,10):
    repeat = stringconversion.count(str(i)) 
    print("The digit ",i," has been repeated " , repeat , " Times. ")