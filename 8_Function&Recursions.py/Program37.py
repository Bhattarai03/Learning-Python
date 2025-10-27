# Write a python function to print first n lines of the following pattern.
'''
***
**
*
'''
def fun():
     x=int(input("Enter a number above zero:"))
     while(x==0):
          fun()
     for  i in range(1,x+1):
          print("*"*x)
          x-=1
     return 0
n=int(input("Enter a number :"))
if n==0:
     print(f"The number is invalid.Reenter a value.")
     fun()

       

def h(n):
    for i in range(1,n+1):
         print("*"*n)
         n-=1

    

h(n)




