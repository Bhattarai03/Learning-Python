# Create a class (2-D vector ) and use it to create another class representing a 3-D vector.
class twoDVec():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"The vector is {self.x}x and {self.y}y")
class threeDvec(twoDVec):
    def  __init__(self,x,y,z):
         super().__init__(x,y)
         self.z=z
    def show(self):
        print(f"The vector is {self.x}x ,{self.y}y and {self.z}z ")
        
p=twoDVec(1,2)
p.show()
q=threeDvec(1,2,3)
q.show()
