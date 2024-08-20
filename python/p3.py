#problem statement: Accept a number as input say X and define a logic to get output say Y. The input can only be 0 or 1 and the output must be 1 if the input is 0 and vice versa
'''
x = int(input("Enter a number , either 0 or 1 : "))
y = 0
if x == 0:
    y = 1
elif x == 1:
    y = 0

print("the value of Y is : ",y)
'''

x = int(input("Enter a number , either 0 or 1 : "))
y = 1 - x

print("the value of Y is : ",y)