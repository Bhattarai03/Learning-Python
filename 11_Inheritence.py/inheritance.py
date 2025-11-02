class Employee():
    company="ITC Hello"
    def show(self,name):
        self.name=name
        print(f"The name  of the master is {self.name}")
a=Employee()


# class Programmer():
#     company="ITC Infotech"
#     def show(self,name):
#         self.name=name
#         print(f"The name is {self.name}")

#     def language(self,language):
#         self.language=language
#         print(f"The Language is {self.language}")

class Coder():
    def salary(self):
        self.salary=143647
        print(f"The salary is {self.salary}")


class Programmer(Employee,Coder):     # This is multiple inheritance
    company="ItC Infotech"
    def language(self,language):
        self.language=language
        print(f"The Language is {self.language}")


a=Employee()
b=Programmer()
print(a.company,b.company)
Programmer.language(b,"Python")
Programmer.show(b,"Raman Raj Bhattrai")
Programmer.salary(b)
print(b.company)   
Programmer.show(b,"Raman")