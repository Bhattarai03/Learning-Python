# This is the code to print the class attributes instead of instance attributes
class employee():
    a=34
    @classmethod
    def show(cls):
        print(f"The class attribute value of a is {cls.a}")

b=employee()
b.a=56
b.show() 