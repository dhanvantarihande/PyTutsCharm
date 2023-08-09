from abc import ABC, abstractmethod
# Abstract - means Incomplete


class Shape:

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):


    def area(self):
        return self.length * self.width


    def perimeter(self):
        return 2 * (self.length * self.width)


rect = Rectangle(2,3)
print(rect.area())
print(rect.perimeter())


class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius


    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(2)
print(circle.area())
print(circle.perimeter())