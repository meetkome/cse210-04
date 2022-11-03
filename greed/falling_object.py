import random
from point import Point
from color import Color

class FallingObject:
    """ A falling object
    This holds appearance, position, points value, movement, and color
    Attributes:
        appearance (str) what we draw
        position (int) where we put the object
        points (int)
        move_counter (int)
        _color (Color)
    """
    FRAME_RATE = 25
    ADD_VELOCITY = 3
    def __init__(self):
        """
        Constructs a new FallingObject
        """
        self.appearance = "0"
        self.position = Point(random.randint(2, 890), 0)
        self.points = 1
        self.move_counter = 0
        self._color = Color(255, 255, 255)

    def fall(self):
        """
        Moves the object
        """
        if self.move_counter < 30:
            self.move_counter += 1
        else:
            self.position.y += 1
            self.move_counter = 0
    
    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color
    
