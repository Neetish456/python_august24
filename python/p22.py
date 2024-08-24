#probelm statement: Write a program to print X shape of N lines.

range = int(input("Enter the number of lines  : "))
for i in range(range):
    for j in range(range):
        if j == i or j == range-i-1:
            print("*",end=" ") 
        else:   
            print(" ",end=" ")
    
    print()
