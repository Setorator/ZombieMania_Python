import zombiemania.settings as settings
from .extractor import extract_all_maps
import pygame as pg

texture_imgs = settings.IMG_DIR + "\\"
EMPTY = "t"
GRASS = "g"
DIRT = "d"
BOX = "#"
SPIKE = "s"
START_SIGN = "Y"
INSTRUCTIONS = "*"
FINISH = "f"
PLAYER = "p"
CREEP = "c"
MAN = "m"
HOUND = "h"


class Map:
    def __init__(self):
        self.tile_size = 16

        # dict with block representations
        self.textures = {GRASS: texture_imgs + "grassblock.png",
                         DIRT: texture_imgs + "dirtblock.png",
                         BOX: texture_imgs + "woodblock.png",
                         SPIKE: texture_imgs + "spikes.png",
                         START_SIGN: texture_imgs + "start.png",
                         INSTRUCTIONS: texture_imgs + "instructions.png",
                         FINISH: texture_imgs + "gateway.gif"}

        self.maps = extract_all_maps()
        self.current_level = self.extract_images(self.maps.pop(0))
        self.map_height = len(self.current_level)
        self.map_width = len(self.current_level[0])

        # Collision map with ids and positions?
        self.objects = {}

    def extract_images(self, map):
        images = []
        for row in range(len(map)):
            r = []
            for col in range(len(map[0])):
                image = None
                if map[row][col] in self.textures:
                    image = pg.image.load(self.textures[map[row][col]])
                r.append(image)
            images.append(r)
        return images

    def update_view(self):
        """
        Meant to update the view when the map is to large to view as a whole
        :return:
        """
        print("NOT YET IMPLEMENTED")


def main():
    print("Creating map")


if __name__ == '__main__':
    main()
