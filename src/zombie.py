from zombiemania.src.sprites import Sprite
from os import path

w_width, w_height = 640, 480


class Zombie(Sprite):
    def __init__(self):
        super(Zombie, self).__init__(size=(48, 63))
        my_path = path.dirname(path.abspath(__file__))
        img_path = path.join(my_path, "..\\res\\img\\zombielookright\\*")
        self.load_images(img_path)

    def move(self):
        if self.rect.left + self.velocity[0] > 0 & self.rect.right + self.velocity[0] <= w_width:
            if self.rect.top + self.velocity[1] > 0 & self.rect.bottom + self.velocity[1] <= w_height:
                self.rect.move_ip(self.velocity[0], self.velocity[1])
