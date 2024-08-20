#accept average score from the student of his exam and print his result as follows:
'''
0 - 49 is Failed
50 - 74 is Second class
75 - 90 is First Class
91 - 1000 is Distinction 
'''

student_result = float(input("Enter the student's score to check for results : "))

if (student_result > 100 and student_result < 0):
    print("Invalid Input ")
else:
    if (student_result >= 91 ):
        print("The result is : Distinction ")
    elif (student_result >= 75 ):
        print("The result is : First Class ")
    elif (student_result >= 50 ):
        print("The result is : Second Class")
    else:
        print("The result is : Fail ")                                           