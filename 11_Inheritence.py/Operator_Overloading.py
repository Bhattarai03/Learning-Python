class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):  # This is for already added vector
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2   # same as v1.__add__(v2)

print(v3)
print(v3)