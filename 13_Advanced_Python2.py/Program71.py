# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,22,33,44,55,66,77,88,99]
def sum(a,b):
    if (a>b):
        return a
    return b
    
print(reduce(sum,l))

