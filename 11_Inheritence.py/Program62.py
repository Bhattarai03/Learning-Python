# Override the __len__()method on vector of program 60 to display the dimension of the vector.
class vector():
    def __init__(self,*args):  # *args allows multiple numbers
        self.l=args

    def __len__(self):
        return len(self.l)
    
v1=vector(2,3,4)
print(len(v1))