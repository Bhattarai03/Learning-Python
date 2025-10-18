# Write a program to print multiplication table of a given number using loop.

a=int(input("Enter a number :"))

# Using for looop

for i in range(1,11):
    b=a*i
    print(f"{a} * {i} = ",b)
    i+=1

# Using While loop
i=1
while(i<11):
    b=a*i
    print(f"{a} * {i} =",b)
    i+=1