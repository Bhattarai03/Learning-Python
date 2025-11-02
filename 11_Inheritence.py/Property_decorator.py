class employee():
    a=34
    @classmethod
    def show(cls):
        print(f"The class attribute value of a is {cls.a}")
    @property    # It allows you to access the method like an attribute instead of calling it like a function.
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

    
b=employee()
b.a=56
b.name="Raman Raj "

print(b.fname,b.lname)
b.show() 
print(b.lname)