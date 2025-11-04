# Type Definition is used to make code readable and also help us to know which data type value does it return from method.

def sum(a:int,b:int)-> int:
    return a+b

# Advance type hint
from typing import List,Tuple,Union,Dict
# List of integers
numbers:List[int]=[1,2,3,4,5,6]

# Tuple of string and integer
person:Tuple[str,int]=("Raman",450)

# Dictionary with string key and integer value
score:dict[str,int]={"raman":45,"Booyah":56}

# Union type of variable which can hold multiple types i.e. either one type or more r type
y:Union[str,int]="id354"
x=12345     # Also valid
y="Raman Raj Bhattarai"
print(y,type(y))
