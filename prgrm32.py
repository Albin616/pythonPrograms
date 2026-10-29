class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if(self.area() > other.area()):
            print("First rectangle has larger area")
        elif self.area() < other.area():
            print("Second rectangle has smaller area")
        else :
            print("Both rectangles have same area")

r1 = Rectangle(10,5)
r2 = Rectangle(6,4)
print("Area of Rectangle 1:",r1.area())
print("Perimeter of Rectangle 1:",r1.perimeter())
print("Area of Rectangle 2:",r2.area())
print("Perimeter of Rectangle 2:",r2.perimeter())
r1.compare(r2)