import pygame

from zombiemania.settings import load_images


class Sprite(pygame.sprite.Sprite):
    """
    The main class of every sprite in the game This class is needed to be able
    to create moving images for the sprites, since the pygame.sprite class
    doesn't support gifs.
    """
    def __init__(self, pos=(300, 200), size=(64, 64)):
        super(Sprite, self).__init__()

        # Members for image handling
        self._images = []
        self._index = 0
        self._image = None
        self.face_delay = 5

        # Members for positioning of the sprite
        self._velocity = [0, 0]
        self._position = [pos[0], pos[1]]
        self._old_position = self.position
        self._jumping = "FALLING"
        self.rect = pygame.Rect(self.position[0],
                                self.position[1],
                                size[0],
                                size[1])
        self.hitbox = pygame.Rect(self.rect.x + self.rect.width * 0.2,
                                  self.rect.y + self.rect.height * 0.2,
                                  self.rect.width * .6,
                                  self.rect.height * .6)

    def draw(self):
        """
        Re-draws the sprite, i.e. updating face etc.
        """
        if self._velocity[0] != 0:
            if self.face_delay == 0:
                self.face_delay = 5
                self._index += 1
                if self._index >= len(self._images):
                    self._index = 0
            else:
                self.face_delay -= 1
        else:
            self._index = 0

        self.image = self._images[self._index]

    def update(self):
        """
        Simple update function calls methods for updating face and position
        """
        self.move()
        self.draw()

    def move(self):
        """
        Simple move function for the sprites, should be overridden by subclasses
        who wants different movements
        """
        self._old_position = self.position[:]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.rect.topleft = self.position
        self.hitbox.midbottom = self.rect.midbottom

    def move_back(self, vertical=False):
        """
        Used for when a collision is detected and the sprite's movement
        is reversed
        """
        self.position = self._old_position
        self.rect.topleft = self.position
        self.hitbox.midbottom = self.rect.midbottom

    def load_images(self, texture):
        """
        Loads the images for a sprite and saves them in the internal image-list
        (Internally uses the global load_images from settings.py
        :param texture: A string representing the texture to load images from
        """

        self._images = load_images(texture)
        self.image = self._images[0]

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        if not value:
            raise ValueError("No valid image for face!")
        self._image = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if len(value) == 2:
            if value[0] is not None:
                self._velocity[0] = value[0]
            if value[1] is not None:
                self._velocity[1] = value[1]
        else:
            raise ValueError("Wrong format for sprite velocity")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if len(value) == 2:
            self._position = list(value)
        else:
            raise ValueError("Wrong format for sprite position")

    @property
    def jumping(self):
        return self._jumping

    @jumping.setter
    def jumping(self, value):
        if value == "FALLING" or value == "GROUND" or value == "UPWARD":
            self._jumping = value
        else:
            raise ValueError("Invalid value for 'jumping': {}".format(value))
