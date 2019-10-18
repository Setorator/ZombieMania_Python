import pygame as pg

import zombiemania.settings as settings
from .extractor import extract_all_maps
from zombiemania.src.map_builder.map_object import MapObject

EMPTY = "t"
PLAYER = "p"
CREEP = "c"
MAN = "m"
HOUND = "h"


class Map:
    def __init__(self):
        self.maps = extract_all_maps()
        self.object_group = pg.sprite.Group()
        self.current_level = self.scan_map(self.maps.pop(0))
        self.map_height = len(self.current_level)
        self.map_width = len(self.current_level[0])

    def scan_map(self, map_file):
        scanned_map = []
        for row in range(len(map_file)):
            tmp_row = []
            for col in range(len(map_file[0])):
                new_map_obj = None
                if map_file[row][col] in settings.textures:
                    new_map_obj = MapObject(map_file[row][col],
                                            (col * settings.tile_size, row * settings.tile_size))
                    self.object_group.add(new_map_obj)
                tmp_row.append(new_map_obj)
            scanned_map.append(tmp_row)
        return scanned_map

    def next_map(self):
        self.current_level = scan_map(self.maps.pop(0))

    def update_view(self):
        """
        Meant to update the view when the map is to large to view as a whole
        :return:
        """
        print("NOT YET IMPLEMENTED")



