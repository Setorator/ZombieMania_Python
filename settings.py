from os import path
from glob import glob
from pygame import image

ROOT_DIR = path.dirname(path.abspath(__file__))
IMG_DIR = glob(ROOT_DIR + "\\**\\img")[0]

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
    FINISH: IMG_DIR + "\\gateway.gif",
    "ZOMBIE": IMG_DIR + "\\zombielookright\\*",
    "BACKGROUND": IMG_DIR + "\\background\\*"
}


def load_images(texture):
    """
    Loads a series of images used for animations into a list.
    Collects the path to the folder from the textures-dict
    :param texture: The name of the texture to collect images for
    :return: A list of the extracted images
    """
    paths = glob(textures[texture], recursive=True)
    images = []
    if len(paths) > 0:
        for tmp_path in paths:
            images.append(image.load(tmp_path).convert())

    return images
