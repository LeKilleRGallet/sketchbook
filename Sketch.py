#create a superclass of a rectangle and a subclass of a square
class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * self.height + 2 * self.width

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

square = Square(5)
print(square.area())
print(square.perimeter())

rectangle = Rectangle(5,10)
print(rectangle.area())
print(rectangle.perimeter())