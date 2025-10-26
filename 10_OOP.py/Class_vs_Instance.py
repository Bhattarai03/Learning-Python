class Employee:
    language = "Python"   # This is a class attributes
    salary=1200000
Raman=Employee()
Raman.name="Raman Raj Bhattarai"   # This is a object attribute
Raman.language="Javascript" # This is a instance  attributes 
print(f" Name is {Raman.name} \n Language is {Raman.language} \n Salary is {Raman.salary}")
# Instance attributes get priority over class attributes