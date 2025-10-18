# Recursion Function

n=int(input("Enter a Number:"))

def fact(n):
     if (n==1 or n==0):
          return 1
     return n * fact(n-1)

print(f"The factorial of the {n} is ",fact(n))
    
    