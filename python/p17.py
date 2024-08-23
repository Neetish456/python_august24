#problem statement: Write a Program to Find Odd(Even) placed digits in a number

inputnum1 = input("Enter the number to find the Even placed digits in a number: ")

even = []
for i in range(len(inputnum1)):
    if i%2 == 0:
        even.append(inputnum1[i])
print("The odd placed digits in the guven number are :",even)
    


#odd 

inputnum2 = input("Enter the number to find the Odd placed digits in a number: ")

odd = []
for i in range(len(inputnum2)):
    if i%2 != 0:
        odd.append(inputnum2[i])
print("The odd placed digits in the guven number are :",odd)