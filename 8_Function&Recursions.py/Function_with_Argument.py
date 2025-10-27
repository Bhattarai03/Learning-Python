#function with argument and with no return value
def func(name,end):
    print("Good Morning," +name)
    print(end)

b=func("Raman",'Thank you')
print(b)

# Function   with argument and return value

def func(name,end="Thanking you"):
    print("Good Morning," +name)
    print(end)
    return("Thanks for choosing us")


a=func("Raman",'Thank you')
print(a)
b=func("Sahil")
print(b)
c=func("Raman")
print(c)

# Function without argument and with return value

def ret():
    a=str(input("Enter a name:"))
    b=str(input("Enter a ending message:"))
    return (f"Good Morning ,{a} \n {b}")
print(ret())

# Function without argument and no return value
def hel():
    a=str(input("Enter a name:"))
    b=str(input("Enter a ending message:"))
    print(f"Good morning, {a} \n {b} ")

hel()