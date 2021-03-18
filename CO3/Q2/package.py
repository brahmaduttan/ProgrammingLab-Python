
import graphics.rectangle
#selective import
from graphics.graphics3D.cuboid import area
#import using *
from graphics.circle import *


l = 25
b = 35
h = 40
r = 7


print("Area of rectangle=",graphics.rectangle.area(l,b))
print("Area of cuboid=",area(l,b,h))
print("Perimeter of circle=",cperimeter(r))
