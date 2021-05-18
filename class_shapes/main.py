class Shapes:

    def __init__(self, type, size):
        self.type = type
        self.size = size

    def Descr(self):
        print(f"{self.type} has a size of :{self.size}")

objShape = Shapes("square", 45)
print(objShape.Descr())


class Rectangle(Shapes):

    def __init__(self, height, width):
        self.heigth = height
        self.width = width

    def area(self):
        result = self.heigth * self.width
        print(f"{result} is the area of a rectangle")

objRect = Rectangle(7,5)
objRect.area()


class Square(Shapes):

    def __init__(self, height, width):
        self.heigth = height
        self.width = width

    def area(self):
        result = self.heigth * self.width
        print(f"{result} is the area of a square")

objSq = Square(12,9)
objSq.area()


class Circle(Shapes):

    def __init__(self, radius):
        self.raduis = radius


    def area(self):
        result = 3.14 * self.raduis **2
        print(f"{result} is the area of a circle")

objCr = Circle(10)
objCr.area()


class Triangle(Shapes):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        result = 0.5 * self.base * self.height
        print(f"{result} is the area of a triangle")

objTr = Triangle(10,5)
objTr.area()
