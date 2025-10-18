# Write a python function to remove a word from a list ad strip it at the same time.

l=["Raman","Sahil","Yurav","Saurav"]

def rem(l,word):
    for item in l:
        l.remove(word)
        return l
    
print(rem(l,"Yurav"))



def add(l,word):
    j=[]
    for item in l:
        if not(item==word):
            j.append(item.strip(word))
    return j

print( add(l,"an"))
