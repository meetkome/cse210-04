import random
from falling_object import FallingObject
from point import Point
from color import Color

class Rock(FallingObject):
    """
    A Rock
    Inherits from FallingObject
    An object that reduces score if Player touches it
    """
    FRAME_RATE = 25
    ADD_VELOCITY = 3
    def __init__(self):
        """
        Constructs a Rock with appearance, points, and color
        """
        super(Rock, self).__init__()
        self.appearance = "0"
        self.points = -1

        r = random.randrange(1,254)
        g = random.randrange(1,254)
        b = random.randrange(1,254) 
        color = Color(r,g,b)       
        super().set_color(color)
