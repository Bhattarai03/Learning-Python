# Write a python function to print first n lines of the following pattern.
'''
***
**
*
'''

n=int(input("Enter a number:"))

def h(n):
    if n==0:
        return("The number is invalid")
    else:
         for i in range(1,n+1):
             
              print("*"* n)
              n-=1

h(n)




