# Store the multiplication tables generated in program in a file named Tables.txt.
n=int(input("Enter a number:"))
l1=[i*n for i in range(1,11)]


with open("Table.txt","a") as f:
    f.write(f"Table of {n}:{str(l1)} \n ")

