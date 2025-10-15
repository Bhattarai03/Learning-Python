# [1,2,3] is the list.
# (1,2,3) is the tuple.

# a=(1) is the integer
# a=(1,)is the tuple

a=(1,2,3,4,5)
print(type(a))

b=(1,3,3,2,3,4,5,3,"Raman","Raj","Bhattarai")
print(type(b))
# Tuple can not be chamged because it is non mutable list.
c=b.count(3)
print(c)
e=b.index(4)
print(e)
f=b*3
print(f)