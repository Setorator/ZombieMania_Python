from os import path

from zombiemania.src.sprites import Sprite

w_width, w_height = 800, 600


class Zombie(Sprite):
    """
    This is the main class of the Zombie (player) character, which is a Sprite.
    """
    def __init__(self):
        super(Zombie, self).__init__(size=(48, 63))
        self.load_images("ZOMBIE")

    def move(self):
        """
        Override of the move() function of the Sprite class used for moving
        the Zombie.
        """
        if self.rect.left + self.velocity[0] > 0 & self.rect.right + self.velocity[0] <= w_width:
            if self.rect.top + self.velocity[1] > 0 & self.rect.bottom + self.velocity[1] <= w_height:
                self.rect.move_ip(self.velocity[0], self.velocity[1])
