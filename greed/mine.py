import random
from falling_object import FallingObject
from color import Color

class Mine(FallingObject):
    """
    A Mine that inherits from FallingObject
    """
    def __init__(self):
        """
        Constructs gem
        Sets appearance, points, and color
        """
        super(Mine, self).__init__()
        self.appearance = "x"
        self.points = -20
        r = random.randrange(1,254)
        g = random.randrange(1,254)
        b = random.randrange(1,254) 
        color = Color(r,g,b)       
        super().set_color(color)
