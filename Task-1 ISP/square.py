# 2D shapes implement AreaCalculate only

from area import AreaCalculate

class Square(AreaCalculate):
    def area(self, *params):
        l = params[0]
        area = l ** 2
        print(f"Area of Square: {area}")