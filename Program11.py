# Write a program to fill a letter template given below with name and date.

a=str(input("Enter a name :"))
b=str(input("Enter a date :"))

c=''' Dear Name
    YOu are  one of the best player in the world
    date
    '''
print(c.replace("Name",a).replace("date",b))