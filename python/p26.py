#problem statement: Write a program to Find the Nth Prime number

inputrange = int(input("Enter the the Nth Term to find the Nth Prime Number : "))
i = 0
primecount = 0
prime = 0
for i in range(0,inputrange+1):

    if i%2 != 0 and i%3 != 0 and i%5 != 0 :
        prime = i
        if primecount == inputrange:
            print("The Nth Prime Number is : ")
        else:
            primecount = primecount + 1




        