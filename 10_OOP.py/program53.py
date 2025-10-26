# Add a static method in problem 51,to greet the user with hello.
class Calculator():
    def num(self,n):
        self.n=n

    @staticmethod
    def func():
        print("Hello Everyone")

    def square(self,n):
        self.square=n*n
        print(f"Square is {self.square}")

    def cube(self,n):
        self.cube=n*n*n
        print(f"Cube is {self.cube}")

    def squareroot(self,n):
        self.squareroot=n**0.5
        print(f"Squareroot is {self.squareroot}")
a=Calculator()
Calculator.square(a,6)
Calculator.cube(a,7)
a.squareroot(36)
a.func()