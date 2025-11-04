# Write a program to display a/b where a and b are integers.If b=0,display infinite by handling the "ZeroDivisionError".
a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))

if (b==0):
    raise ZeroDivisionError("hey our program is not meant to divided numbers by zero.")
else:
    print(f"The division a/b is {a/b}")

