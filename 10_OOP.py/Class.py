class Employee:
    language = "Python"   # This is a class attributes
    salary=1200000
Raman=Employee()
Raman.name="Raman Raj Bhattarai"   # This is a instance attribute
print(f" Name is {Raman.name} \n Language is {Raman.language} \n Salary is {Raman.salary}")
#  Here name is a object attributes and salary and language are class
#  attributes as they directly belong to the class.