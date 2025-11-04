# Write a program to input name,marks and phone number of a student and format it using the format function like before.

name=str(input("Enter a name:"))
marks=float(input("Enter your marks:"))
Ph_no=int(input("Enter your phone number:"))

b="Name:{} \n Marks :{} \n Phone No:{}".format(name,marks,Ph_no)
print(b)