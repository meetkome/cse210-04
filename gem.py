import random
from falling_object import FallingObject
from point import Point
from color import Color

class Gem(FallingObject):
    def __init__(self):
        super(Gem, self).__init__()
        self.appearance = "*"
        self.points = 1

        r = random.randrange(5,232)
        g = random.randrange(20,35)
        b = random.randrange(5,173) 
        color = Color(r,g,b)       
        super().set_color(color)