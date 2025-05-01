# 2D shapes implement AreaCalculate only
from area import AreaCalculate

class Circle(AreaCalculate):
    def area(self, *params):
        r = params[0]
        area = 3.14 * r**2
        print(f"Area of Circle: {area}")