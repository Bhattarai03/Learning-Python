# Write a program to print the multiplication table of given number.

a=int(input("Enter a number:"))

def mul(a):
    if(a<=0):
        return("The number is invalid")
    else:
         for i in range(1,11):
             print(f"{a}*{i} =",a*i)

mul(a)
         
  

       