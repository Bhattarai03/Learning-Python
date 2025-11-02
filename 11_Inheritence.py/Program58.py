# Create a class 'Employee and add salary and increment properties to it.
class Employee():
    salary = 234
    increment= (20)/100
    

    @property
    def increinsalary(self):
        return (self.salary + (self.salary * self.increment))
    
    @increinsalary.setter
    def increinsalary(self,new_salary):
        self.increment=(((new_salary/self.salary)-1)*100)

e=Employee()
print(f"The salary after increment is {e.increinsalary}")

print(e.increment)

