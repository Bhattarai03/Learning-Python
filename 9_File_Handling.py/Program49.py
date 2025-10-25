# Write a program to rename the file using python.
with open("File2.txt") as g :
    c2 = g.read()

with open("Rename.txt","w") as g :
    g.write(c2)

import os
os.remove("File2.txt")