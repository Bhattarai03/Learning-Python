a=89   # This is a global variable
def func():
     a=45 # This is a local varaible .To make this local variable into global ,add global syntax
     return a
print(func())




def fun():
    global a 
    a=56
    return a
print(fun())
print(a)
print(func())
