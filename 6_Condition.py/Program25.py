# Write a program to calculate the grade of the student  from the marks.

a=float(input("Enter the marks:"))

if(a>90):
    print("the grade is A+")
elif(a>80 and a<90):
    print("The grade is A")
elif(a>70 and a<80):
    print("The garde is B+")
elif(a>60 and  a<70):
    print("The grade is B")
elif(a>50 and a<60):
    print("The grade is C+")
elif(a>40 and a<50):
    print("The grade is D")
else:
    print("student fails")