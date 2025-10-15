# Write a program to accept marks of 6 students and display them in a sorted manner.

mark=[]
a=float(input("Enter a mark of 1st student : "))
b=float(input("Enter a mark of 2nd student : "))
c=float(input("Enter a mark of 3rd student : "))
d=float(input("Enter a mark of 4th student : "))
e=float(input("Enter a mark of 5th student : "))
f=float(input("Enter a mark of 6th student : "))

mark.append(a)
mark.append(b)
mark.append(c)
mark.append(d)
mark.append(e)
mark.append(f) 


mark.sort()
print(mark)

x=mark.count(45)
print(x)


print(sum(mark))
# It is for addition of all object in a list
