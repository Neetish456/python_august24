#numofcust = int(input("Enter the number of customers : "))
bill = [9, 14, 25, 17, 36, 50, 49, 62, 64, 81, 90, 100, 121, 15, 144, 200]
def perf_square(num):
    squareroot = int(num**0.5)
    return squareroot**2 == num
count = 0
for i in bill:
    if perf_square(i):
        count = count + 1 
        print(i)
print("The numbers of customers that'll be getting a discount is : ",count)