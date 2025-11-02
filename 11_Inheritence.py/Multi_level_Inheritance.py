class Employee:
    a=2

class Programmer(Employee):
    b=3

class Manager(Programmer):
    c=5

o=Employee()
print(o.a)    

d=Programmer()
print(d.b)
print(d.a)

e=Manager()
print(e.a,e.b,e.c)