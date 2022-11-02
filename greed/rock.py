import random
from falling_object import FallingObject
from point import Point
from color import Color

class Rock(FallingObject):
    def __init__(self):
        super(Rock, self).__init__()
        self.appearance = "0"
        self.points = -1

        speed = random.randrange(1,16)
        super().set_velocity(Point(0,speed))

        r = random.randrange(200,255)
        g = random.randrange(128,175) 
        color = Color(r,g,g)       
        super().set_color(color)
