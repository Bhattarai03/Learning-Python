# Create a Class "Programmer" for storing information of few programmers working in microsoft.
class Programmer():
    office="Microsoft"

    def __init__(self,name,language,salary,age,role):
        self.name=name
        self.language=language
        self.salary=salary
        self.age=age
        self.role=role

raman=Programmer("Raman Raj Bhattarai","Python",10000000,19,"Senior Ai Security Engineer")       
print(f"Name:{raman.name}\n Language:{raman.language}\n Salary:Rs{raman.salary}\nAge:{raman.age}\n Role:{raman.role}")