# Write a program to greet all the person names stored in a list "l" and which starts with s.

l=["Raman","Sohan","Sachin","Rahul"]

for i in range(0,4):

    if l[i].startswith("S"):
        print("Nice to meet you",l[i])

