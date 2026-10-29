class Square:
    def __init__(self, side ):
        self.side = side


    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4* self.side

    def compare(self, other):
        if self.area() > other.area():
            print("First Square has larger area")
        elif self.area() < other.area():
            print("Second Square has larger area")
        else:
            print("Both Square have equal area")


r1 = Square(10)
r2 = Square(6)
print("Area of Square 1:", r1.area())
print("Perimeter of Square 1:", r1.perimeter())
print("Area of Square 2:", r2.area())
print("Perimeter of Square 2:", r2.perimeter())
r1.compare(r2)
