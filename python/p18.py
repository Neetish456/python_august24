#porblem Statement : Write a Program to Find Odd placed Even digits in a number.
inputnum1 = input("Enter the number to find odd place even digits:")
odd1 = []
for i in range(len(inputnum1)):
    if i%2 == 0:
        if int(inputnum1[i])%2 == 0:
            odd1.append(inputnum1[i])
print("The odd placed even digits in the given number are :",odd1)