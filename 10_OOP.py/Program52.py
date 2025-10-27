# Create  a class with a class attribute a ,create a object from it and set "a" directly using object.a=0.Does this change attributes?
class abc():
     a=6


obj=abc()
print(obj.a)  # Print the class attributes because instance attributes is not present.
obj.a=0  # It is a instance attribute.
print(obj.a)  # Print the instance attributes.
print(abc.a)  # Print the class attribute