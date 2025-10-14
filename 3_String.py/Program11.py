# Write a program to fill a letter template given below with name and date.

a=str(input("Enter a name :"))
b=str(input("Enter a date :"))

d=a.title()
c=''' Dear Name
    YOu are  one of the best player in the world
    date
    '''
print(c.replace("Name",d).replace("date",b))