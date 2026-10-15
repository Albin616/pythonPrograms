square=lambda side:side*side
rectangle=lambda length,breadth:length*breadth
triangle=lambda base,height:0.5*base*height
side=float(input("Enter the side of the square:"))
print("Area of square:",square(side))
length=float(input("Enter the length of the rectangle:"))
breadth=float(input("Enter the breadth of the rectangle:"))
print("Area of rectangle:",rectangle(length,breadth))
base=float(input("Enter the base of the triangle:"))
height=float(input("Enter the height of the triangle:"))
print("Area of triangle:",triangle(base,height))