
f=open("file.txt")
data=f.read()
print(data)
f.close()

# The same code can be written as :
with open("file.txt") as f:
    print(f.read())
