# Write a class 'Vector' representing a vector of n dimensions.Overload the '+' and '*' operator which calculates the sum and the dot product of them.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # Dot product gives scalar
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v3 = Vector(3, 5, 6)

print("Addition:", v1 + v2 + v3)
print("Dot Product (v1·v2):", v1 * v2)

