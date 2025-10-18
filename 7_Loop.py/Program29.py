# Write a program to find whether  a given number is prime or not.

a=int(input("Enter a number:"))
b=0
for i in range(1,a+1):
    if (a%i==0):
        b=b+1
    i+=1

if(b==2):
    print("The number is prime number.")
else:
    print("The number is composite number.")
