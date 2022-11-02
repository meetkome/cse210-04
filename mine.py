from falling_object import FallingObject

class Mine(FallingObject):
    def __init__(self):
        super(Mine, self).__init__()
        self.appearance = "x"
        self.points = -20