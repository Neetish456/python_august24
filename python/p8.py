#problem statement: Write a program to check if the user given year is a Leap year.
print("This program checks for Leap year.")
year = int(int("Enter the year : "))
 if ((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)):  
    print("The given year is a leap year.") 

