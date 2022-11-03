from pyray import *

class Score:
    """
    Score
    Keeps track of how many points the Player has earned
    """
    def __init__(self):
        """
        Constructs Score with value
        """
        self.value = 0
        
    def display_score(self):
        """
        Shows you your score
        """
        draw_text(f"Score: {self.value}", 20, 20, 25, WHITE)
        
    def update_score(self, points):
        """
        Changes the value of your score
        """
        self.value += points