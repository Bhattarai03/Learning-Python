# Create a class "pets" from a class 'Animal 'and further create a 'Dog' from 'Pets'.Add a method 'bark' to class 'dog'.
class Animal():
    def  __init__(self):
        pass

class Pets(Animal):
    def __init__(self):
        super().__init__()
    def __init__(self):
        pass
class Dogs(Pets):
    def __init__(self):
        super().__init__()
    @staticmethod
    def bark():
        return ("Bbow Bbow")

d=Dogs()
print(d.bark())