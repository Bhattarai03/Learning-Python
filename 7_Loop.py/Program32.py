# Write a program to print following pattern.
'''
*
***
*****
'''
j=0
for i in range(1,4):
    print(("*"*i)+ j*"*")
    i+=1
    j=j+1



'''
*
**
***
'''

for i in range(1,4):
    print("*"*i)
    i+=1


'''
***
* *
***
'''

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")


