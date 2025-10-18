#function with argument 
def func(name,end):
    print("Good Morning," +name)
    print(end)

func("Raman",'Thank you')

# Function with return value

def func(name,end="Thanking you"):
    print("Good Morning," +name)
    print(end)
    return("Thanks for choosing us")


a=func("Raman",'Thank you')
b=func("Sahil")

print(a)

