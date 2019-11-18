
from zombiemania.src.sprite import Sprite

w_width, w_height = 800, 600


class Zombie(Sprite):
    """
    This is the main class of the Zombie (player) character, which is a Sprite.
    """
    def __init__(self):
        super(Zombie, self).__init__(size=(48, 63))
        self.load_images("ZOMBIE")
