# Write a program to find the greatest of four numbers entered by the user.

 # 1st method
a=int(input("Enter a Number:"))
b=int(input("Enter a Number:"))
c=int(input("Enter a Number:"))
d=int(input("Enter a Number:"))

if(a>b):
    if(a>c):
        if(a>d):
            print("a is the greatest number")

if(b>a):
    if(b>c):
        if(b>d):
            print("b is the greatest number")

if(c>a):
    if(c>b):
        if(c>d):
            print("c is the greatest number")

if(d>b):
    if(d>c):
        if(d>a):
            print(" d is the greatest number")

# 2nd method

if(a>b and a>c and a>d):
    print("a is the greatest")

elif(b>a and b>c and b>d):
    print("b is the greatest")

elif(c>a and c>b and c>d):
    print("c is the greatest")
else:
    print("d is the greatest")



