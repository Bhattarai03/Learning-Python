# Write a python function to remove a word from a list ad strip it at the same time.

l=["Raman","Sahil","Yurav","Saurav","palpa"]

def rem(l,word):
    for item in l:
        l.remove(word)
        return l
    
print(rem(l,"Yurav"))



def add(l,word):
    j=[]
    for item in l:
        if (item!=word):
            j.append(item.strip(word))
            # Strip is used for removing the specific character from begining or from ending , not from the middle.
    return j

print( add(l,"pa"))
