# Write a program to indentify whether the content of two file are identical or not.

with open("File1.txt") as f :
    c1 = f.read()

with open("File2.txt") as g :
    c2 = g.read()

if (c1 == c2):
    print("Yes these files are identical")
else:
    print("No these files are not identical")

