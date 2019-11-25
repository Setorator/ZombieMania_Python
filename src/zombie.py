
from zombiemania.src.sprite import Sprite

class Zombie(Sprite):
    """
    This is the main class of the Zombie (player) character, which is a Sprite.
    """
    def __init__(self):
        super(Zombie, self).__init__(size=(64, 128))
        self.load_images("ZOMBIE")
        self.gravity = 5  # positive since y increases down
        self.jump_height = 128  # jump height i # pixels
        self.start_jump = 0

    def move(self):

        self._old_position = self.position[:]
        self.position[0] += self.velocity[0]

        # Gravity control for when jumping.
        if self.jumping == "UPWARD":
            if self.position[1] < (self.start_jump - self.jump_height):
                self.velocity[1] = self.gravity
                self.jumping = "FALLING"
            else:
                self.velocity[1] = -10
        elif self.jumping == "FALLING":
            self.velocity[1] = self.gravity
        elif self.jumping == "GROUND" and self.velocity[1] < 0:
            self.jumping = "UPWARD"
            self.start_jump = self.position[1]
        else:
            self.velocity[1] = 0

        self.position[1] += self.velocity[1]
        self.rect.topleft = self.position
        self.hitbox.midbottom = self.rect.midbottom

    def move_back(self, vertical=True):
        """
        Special move_back needed for when jumping and colliding with a roof
        """

        if vertical:
            if self._old_position[1] > self.position[1]:
                self.jumping = "FALLING"

            elif self._old_position[1] < self.position[1]:
                self.jumping = "GROUND"
            self.position[1] = self._old_position[1]
        else:
            self.position[0] = self._old_position[0]

        self.rect.topleft = self.position
        self.hitbox.midbottom = self.rect.midbottom

        """
        move back one direction at a time
        if collision gone, no probs
        otherwise move the other direction
        """
