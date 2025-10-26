class Employee:
    language = "Python"   # This is a class attributes
    salary=1200000


    def __init__(self,name,language,salary):   #It is dunder method,which is automatically called.
         print("Hello every one ,I am Raman Raj Bhattarai.")
         self.name=name
         self.language=language
         self.salary=salary

    
    @staticmethod   # It mean we do not need any properties from the object.
    def hello():    # No self because we don't  need properties from the object.
        print("Good morning")
        


Rohan=Employee("Rohan","Javascript",1300000)
print(Rohan.name,Rohan.language,Rohan.salary)
Rohan.hello()
