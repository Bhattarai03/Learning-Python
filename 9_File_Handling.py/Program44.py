# A file contains a word "Donkey" multiple times .You need to write a program which replace this ****** by updating a same file.

with open("Program44.txt") as f:
    text=f.read()

d=text.replace("Donkey","******").replace("donkey","******")

with open("Program44.txt","w") as f:
     f.write(d)
    

