# Write a program to find out whether a student has passed or failed .if it required a total of 40% and at leaast 33% in each subject to pass .Assume 3 subjects and take marks as input from the user.

a=float(input("Enter a marks:"))
b=float(input("Enter a marks:"))
c=float(input("Enter a marks:"))

d=((a/100)*100)
e=((b/100)*100)
f=((c/100)*100)

if(d>33):
    print("The student is pass ")
else:
    print("The student is fail")

if(e>33):
    print("The student is pass")
else:
    print("The student is fail")

if(f>33):
    print("The student is pass")
else:
    print("The student is fail")

i=((a+b+c)/300)*100
if(i>40):
    print("The student has passed this exam")

else:
    print("The student has failed this exam")