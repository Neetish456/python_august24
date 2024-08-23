#problem statement: Write a program to check if the number is a Perfect square.
import math

print("This program checks if the given number is a perfect square.")
number1 = int(input("Enter the number : "))

square_root = math.sqrt(number1)

perfect_square = float(square_root**2)
if number1 == perfect_square :
    print("The given number is a perfect square. ")

'''
print("This program checks if the given number is a perfect square.")
number1 = int(input("Enter the number : "))

square_root = number1**0.5

perfect_square = float(square_root**2)
if number1 == perfect_square :
    print("The given number is a perfect square. ")

'''



