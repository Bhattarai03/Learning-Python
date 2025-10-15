
friend=["apple","Tea",5,654.87,"aakash","banana","rohan"]

print(friend[0:4]) # The syntax is same for both list and string.
 
friend[3] ="Bikash"  # It is used to changed the name of the object in the list.
print(friend)

# When you add string functionlity in the string ,it simply created a new string but  in the context of list it just  replace the text.
# String is non mutable but list is mutable.

friend.append("harry") # Add new object in the list
print(friend)

a=[1,2,5,7,3,4,6,9,0,8]
a.sort()  # Ascending order
print(a)
b=[0,6,7,8,3,4,5,1,2]
b.reverse() # For reversing the list
print(b)
b.insert(4,45) # It is used to insert the object in the middle or where ever they want
print(b)
c=[2,3,4,5,6,7,8,2,1]
print(c.pop(3)) # Used to print the specific value in the list  and also delete the same object from the list.
print(c)
d=[1,2,3,4,5,6,7,8]
d.remove(6)  # Used to remove the object form the list
print(d)