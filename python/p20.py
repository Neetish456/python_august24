#problem statement: Write a Program to print the Equi Lateral Triangle of N lines.

lines = int(input("Enter the number of lines : "))
for i in range(0,lines+1):
    for j in range(0,i+1):
        print("\t")
    print("*"*i)
    print("\n")