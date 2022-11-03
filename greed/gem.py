import random
from falling_object import FallingObject
from point import Point
from color import Color

class Gem(FallingObject):
    """
    A Gem that inherits from FallingObject
    It changes appearance and points
    It also sets color
    """
    def __init__(self):
        """
        Constructs Gem
        """
        super(Gem, self).__init__()
        self.appearance = "*"
        self.points = 1

        r = random.randrange(1,254)
        g = random.randrange(1,254)
        b = random.randrange(1,254) 
        color = Color(r,g,b)       
        super().set_color(color)