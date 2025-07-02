class Rectangle:
     def __init__(self, width, height):
         self.width = width
         self.height = height
     def area(self):
         return self.width * self.height
     def perimetr(self):
        return 2 * (self.width + self)
 class Square(Rectangle):
     def __init__(self, side):
         super().__init__(side, side)
         self.side = side
     def area(self):
         return self.side ** 2

     def perimetr(self):
       return 4 * self.side

 rect = Rectangle(4, 5)
print("Площадь прямоугольника:", rect.area())
print("Периметр прямоугольника:", rect.perimetr())
sq = Square(3)
print("Площадь квадрата:", sq.area())
print("Периметр квадрата:", sq.perimetr())