class Circle:
    def __init__(self, radius ):
        self.radius = radius


    def area(self):
        return 3.14*(self.radius**2)

    def perimeter(self):
        return 2*3.14* self.radius

    def compare(self, other):
        if self.area() > other.area():
            print("First Circle has larger area")
        elif self.area() < other.area():
            print("Second Circle has larger area")
        else:
            print("Both Circle have equal area")


r1 = Circle(10)
r2 = Circle(6)
print("Area of Circle 1:", r1.area())
print("Perimeter of Circle 1:", r1.perimeter())
print("Area of Circle 2:", r2.area())
print("Perimeter of Circle 2:", r2.perimeter())
r1.compare(r2)
