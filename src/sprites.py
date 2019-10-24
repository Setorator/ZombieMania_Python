import pygame

from zombiemania.settings import load_images


class Sprite(pygame.sprite.Sprite):
    """
    The main class of every sprite in the game This class is needed to be able
    to create moving images for the sprites, since the pygame.sprite class
    doesn't support gifs.
    """
    def __init__(self, pos=(100, 100), size=(64, 64)):
        super(Sprite, self).__init__()
        self._images = []
        self._index = 0
        self._image = None
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self._velocity = [0, 0]

    # TODO: make a "draw" function instead
    def update(self):
        """
        Simple update function which rotates the images of the sprite.
        """
        self._index += 1
        if self._index >= len(self._images):
            self._index = 0
        self._image = self._images[self._index]
        self.move()

    def move(self):
        """
        Simple move function for the sprites, should be overridden by subclasses
        who wants different movements
        """
        self.rect.move_ip(self._velocity[0], self._velocity[1])


    def load_images(self, texture):
        """
        Loads the images for a sprite and saves them in the internal image-list
        (Internally uses the global load_images from settings.py
        :param texture: A string representing the texture to load images from
        """

        self._images = load_images(texture)
        self._image = self._images[0]

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, img):
        if not img:
            raise ValueError("No valid image for face!")
        print("Setting face for {}".format(self.__repr__()))
        self._image = img

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, d_vec):
        """
        # TODO: rewrite to match behaviour
        Changes the velocity of the sprite
        :param dx: Change in x-direction (positive right)
        :param dy: Change in y-direction (positive down)
        """
        if d_vec[0] is not None:
            self._velocity[0] = d_vec[0]
        if d_vec[1] is not None:
            self._velocity[1] = d_vec[1]
