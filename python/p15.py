#porblem statement: Write a Program to find Sum of even(odd) digits in a number.
inputnum1 = input("Enter the number to find the Sum of even digits in a number: ")
even_sum = 0
for i in inputnum1:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        continue
print("the Sum of even digits in given number is  : ", even_sum)

#odd

inputnum1 = input("Enter the number to find the Sum of odd digits in a number: ")
odd_sum = 0
for i in inputnum1:
    if i % 2 != 0 :
        odd_sum = odd_sum + i
    else:
        continue
print("the Sum of odd digits in given number is  : ", odd_sum)