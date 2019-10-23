from os import path
from glob import glob

ROOT_DIR = path.dirname(path.abspath(__file__))
IMG_DIR = glob(ROOT_DIR + "\\**\\img")[0]

tile_size = 16

EMPTY = "t"
GRASS = "g"
DIRT = "d"
BOX = "#"
SPIKE = "s"
START_SIGN = "Y"
INSTRUCTIONS = "*"
FINISH = "f"

# dict with block representations
textures = {
    GRASS: IMG_DIR + "\\grassblock.png",
    DIRT: IMG_DIR + "\\dirtblock.png",
    BOX: IMG_DIR + "\\woodblock.png",
    SPIKE: IMG_DIR + "\\spikes.png",
    START_SIGN: IMG_DIR + "\\start.png",
    INSTRUCTIONS: IMG_DIR + "\\instructions.png",
    FINISH: IMG_DIR + "\\gateway.gif"
}
