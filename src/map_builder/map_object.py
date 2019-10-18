import pygame as pg

import zombiemania.settings as settings


class MapObject(pg.sprite.Sprite):
    def __init__(self, tile=settings.DIRT, pos=(100, 100)):
        super(MapObject, self).__init__()
        self._tile_type = tile
        self.pos = self.x_pos, self.y_pos = pos[0], pos[1]
        self.tile_size = 16
        self._image = pg.image.load(settings.textures[self.tile_type])
        self.rect = pg.Rect(self.x_pos, self.y_pos, self.tile_size, self.tile_size)

    @property
    def tile_type(self):
        return self._tile_type

    @property
    def image(self):
        return self._image
