
from zombiemania.src.sprite import Sprite


class Zombie(Sprite):
    """
    This is the main class of the Zombie (player) character, which is a Sprite.
    """
    def __init__(self):
        super(Zombie, self).__init__(size=(64, 128))
        self.load_images("ZOMBIE")
