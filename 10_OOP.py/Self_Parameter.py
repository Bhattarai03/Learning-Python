class Employee:
    language = "Python"   # This is a class attributes
    salary=1200000

    def func(self):
         print(f" Name is {Raman.name} The language is {self.language} and salary is {self.salary}")
    
    @staticmethod   # It mean we do not need any properties from the object.
    def hello():    # No self because we don't  need properties from the object.
        print("Good morning")
        
Raman=Employee()
Raman.name="Raman Raj Bhattarai"   # This is a instance attribute
# Raman.func() and Employee.func(Raman) are same.
# The Raman.func() is represented as Employee.func(Raman) by python automatically.
Employee.func(Raman)
Raman.hello()
