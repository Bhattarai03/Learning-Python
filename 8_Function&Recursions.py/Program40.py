# Write a program to print the multiplication table of given number.

a=int(input("Enter a number:"))

def mul(a):
    if(a<=0):
        return("The number is invalid")
    else:
         for i in range(1,11):
             print(f"{a}*{i} =",a*i)

b=mul(a)
print(f"Value:{b},\n If the value is none .It means the number is greater than zero.\n Otherwise the number is invalid")
         
  

       