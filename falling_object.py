import random
from point import Point
from color import Color

class FallingObject:
    def __init__(self):
        self.appearance = "0"
        self.position = Point(random.randint(2, 890), 0)
        self.points = 1
        self.move_counter = 0
        self._color = Color(255, 255, 255)

    def fall(self):
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
    
