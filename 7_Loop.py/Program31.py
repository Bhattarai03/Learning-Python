# Write a program to calculate the factorial of a given number using loop.

a=int(input("Enter a number:"))
fact=1

for i in range(1,a+1):
    fact=fact*i
    i+=1
print("The factorial of the given number is ",fact)

 

