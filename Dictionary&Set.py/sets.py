e = {1,2,3,4,4,5}
a=set()    # It is the empty set 
x={ }   # Don't  use this for creating empty set ,this will create empty dictionary
print(e)

# Methods of sets
e.add(54)
print(e,type(e))
e.remove(4)
print(e,type(e))
e.pop() # It is used to remove random object in the set
print(e)

# Example of list to avoid confusion
c=[1,2,3,4,5,6,7,8,9]
print(c,type(c))
c.append(69)
print(c)
 
#  Example of tuple to avoid confusion
d=(1,2,4,5,6,7,5,3)
print(d,type(d))

# Set Union Intersection
q={1,2,3,4,5}
r={3,7,8,5,90,45}
t={2,3,4,5,6,7}
print(q.union(r))

# Set intersection
print(q.intersection(r,t))

# It is used to update the set only keeping the object that are common in all set
q.intersection_update(r,t)
print(q)
