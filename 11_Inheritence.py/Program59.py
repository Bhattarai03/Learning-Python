# Write a class 'Complex' to represent complex numbers,along with overloaded operators'+' and '*' which add and multiple them.
class Complex():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __add__(self,other):
        return Complex (self.a +other.a , self.b+other.b)
    
    def __str__(self):
        return  f"complex number :{self.a}+{self.b}i"
    
    def __mul__(self,other):
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return Complex(real, imag)
    def __str__(self):
        return  f"complex number :{self.a}+{self.b}i"
    
c1=Complex(2,3)
c2=Complex(4,5)

c3=c1+c2
c4= c1 * c2

print(c3)
print(c4)