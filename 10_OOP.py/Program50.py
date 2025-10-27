# Create a Class "Programmer" for storing information of few programmers working in microsoft.
class Programmer():
    office="Microsoft"

    def __init__(self,name,language,salary,age,role):
        self.name=name
        self.language=language
        self.salary=salary
        self.age=age
        self.role=role
        print(f"Name:{self.name}\n Language:{self.language}\n Salary:Rs{self.salary}\nAge:{self.age}\n Role:{self.role}")

raman=Programmer("Raman Raj Bhattarai","Python",10000000,19,"Senior Ai Security Engineer")

ram=Programmer("Raman Raj ","Python",10000000,19,"Senior Ai Security Engineer")