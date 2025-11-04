# This file is just  for showing example of importing this func() to another module.
def func():
    return f"Hello world"
print(func())


if __name__=='__main__':
    # If this code is directly executeed by running this file its present in
    print("We are directly running this code")
    print(__name__)

# This above code only executed by me .If somebody else is importing this function it simply does not execute the code.