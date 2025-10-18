# Write a program to print multiplication table of n using for loops in reversed order.

a=int(input("Enter a number:"))

b=10

for i in range(1,11):
    print(f"{a}*{b}={a*b}")
    i+=1
    b-=1