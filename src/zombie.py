from zombiemania.src.sprites import Sprite
from os import path

class Zombie(Sprite):
    def __init__(self):
        super(Zombie, self).__init__(size=(48, 63))
        my_path = path.dirname(path.abspath(__file__))
        img_path = path.join(my_path, "..\\res\\img\\zombielookright\\*")

        self.load_images(img_path)