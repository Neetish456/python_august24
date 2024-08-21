#problem statement: Write a program to print Math table of a Number.
print("This Program prints Math Multiplication Table of the given number.")
number1 = int(input("Enter the number : "))
length1 = int(input("Enter the lenght of the math table : "))

for i in range(1,length1 + 1):
    print(number1 , " X ", i , " = ",number1*i)
