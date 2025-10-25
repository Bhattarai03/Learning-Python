# Repeat program 44 for a list of such words to be censored.

with open("Program44.txt") as f:
    text=f.read()

d=text.replace("Honey","******").replace("honey","******").replace("Sugar","*****").replace("sugar","*****")

with open("Program44.txt","w") as f:
     f.write(d)
    