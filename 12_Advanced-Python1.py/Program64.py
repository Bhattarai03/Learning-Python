# Write a program to print third,fifth and seventh element form a list  using enumerate function.
l=[1,2,3,4,5,6,89,67,45,34,32,35]
for i,item in enumerate(l):
    if i==2 or i==6 or i==4 :
        print(f"The number at index {i} is {item}")
     