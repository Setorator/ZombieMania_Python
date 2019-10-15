import pygame
import glob
import os

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos=(100, 100), size=(64, 64)):
        super(Sprite, self).__init__()
        self._images = []
        self._index = 0
        self._image = None
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self._velocity = [0, 0]

    def update(self):
        self._index += 1
        if self._index >= len(self._images):
            self._index = 0
        self._image = self._images[self._index]
        self.rect.move_ip(self._velocity[0], self._velocity[1])

    def load_images(self, folder_path):
        paths = glob.glob(folder_path, recursive=True)
        if len(paths) > 0:
            for path in paths:
                self._images.append(pygame.image.load(path))
            self._image = self._images[0]

    @property
    def image(self):
        #print("Getting face for {}".format(self.__repr__()))
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
