# Write a program to find whether a given username contain less than 10 character or not.

a=str(input("Enter a username:"))

if(len(a)<=10):
    print("The username contain less than equal to 10  character")
else:
    print("The username is fine")