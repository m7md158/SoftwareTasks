from volume import VolumeCalculate 
from area import AreaCalculate

class Cylinder(VolumeCalculate, AreaCalculate):
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