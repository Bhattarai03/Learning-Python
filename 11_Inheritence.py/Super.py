class Employee:
    def __init__(self):
        
        print("Constructor of Employee")
    a=2

class Programmer(Employee):
     def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
     b=3

class Manager(Programmer):
     def __init__(self):
        super().__init__()
        print("Constructor of Manager")
     c=5

o=Employee()
print(o.a)    
d=Programmer()
print(d.b)
print(d.a)

e=Manager()
print(e.a,e.b,e.c)