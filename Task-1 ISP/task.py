from abc import ABC, abstractmethod

# Separate interfaces
class AreaCalculate(ABC):
    @abstractmethod
    def area(self, *params):
        pass

class VolumeCalculate(ABC):
    @abstractmethod
    def volume(self, *params):
        pass

# 2D shapes implement AreaCalculate only
class Circle(AreaCalculate):
    def area(self, *params):
        r = params[0]
        area = 3.14 * r**2
        print(f"Area of Circle: {area}")

class Square(AreaCalculate):
    def area(self, *params):
        l = params[0]
        area = l ** 2
        print(f"Area of Square: {area}")

# 3D shapes implement both if needed
class Cylinder(AreaCalculate, VolumeCalculate):
    def area(self, *params):
        r = params[0]
        h = params[1]
        area = 2 * 3.14 * r * (r + h)
        print(f"Surface Area of Cylinder: {area}")

    def volume(self, *params):
        r = params[0]
        h = params[1]
        volume = 3.14 * r * r * h
        print(f"Volume of Cylinder: {volume}")


# Run 

if __name__ == '__main__':
    square = Square()
    square.area(5)  # side = 5

    circle = Circle()
    circle.area(3)  # radius = 3

    cylinder = Cylinder()
    cylinder.area(2, 5)  # radius = 2, height = 5
    cylinder.volume(2, 5)


