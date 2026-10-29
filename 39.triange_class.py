class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def compare(self, other):
        if self.area() > other.area():
            print("First Triangle has larger area")
        elif self.area() < other.area():
            print("Second Triangle has larger area")
        else:
            print("Both Triangles have equal area")


t1 = Triangle(10, 6, 10, 8, 6)
t2 = Triangle(8, 4, 8, 5, 5)

print("Area of Triangle 1:", t1.area())
print("Perimeter of Triangle 1:", t1.perimeter())

print("Area of Triangle 2:", t2.area())
print("Perimeter of Triangle 2:", t2.perimeter())

t1.compare(t2)