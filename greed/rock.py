from falling_object import FallingObject

class Rock(FallingObject):
    def __init__(self):
        super(Rock, self).__init__()
        self.appearance = "0"
        self.points = -1