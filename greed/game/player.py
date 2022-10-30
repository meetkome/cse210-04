from game.actor import Actor
class Player(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""
    
    def get_message(self):
        return self._message
    
    def set_message(self, message):
        self._message = message