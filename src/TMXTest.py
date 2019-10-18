import pygame
import pyscroll
from pytmx.util_pygame import load_pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('../res/img/zombielookright/frame_00_delay-0.2s.png').convert_alpha()
        # .convert_alpha allows for transparency around you character
        self.velocity = [0, 0]
        self._position = [0, 0]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * .5, 8)

    def position(self):
        return list(self._position)

    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        """ If called after an update, the sprite can move back to give the
            illusion of the sprite not moving.
        """
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

class Game:

    def __init__(self):
        # load data from pytmx
        self.filename = "../res/maps/TestMap.tmx"
        tmx_data = load_pygame(self.filename)

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)

        w, h = screen.get_size()

        # create new renderer (camera)
        # clamp_camera is used to prevent the map from scrolling past the edge
        self.map_layer = pyscroll.BufferedRenderer(map_data,
                                                   (w / 2, h / 2),
                                                   clamp_camera=True)

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)
        # I use "from pyscroll.group import PyscrollGroup", if you do this don't use the pyscroll bit above.
        self.zombie = Zombie()

        # add our hero to the group
        self.group.add(self.zombie)

    def draw(self, surface):
        self.group.center(self.zombie.rect.center)
        self.group.draw(surface)

    def run(self):
        scale = pygame.transform.scale

        try:
            self.draw(temp_surface)
            scale(temp_surface, screen.get_size(), screen)
            pygame.display.flip()

        except:
            pygame.quit()


# simple wrapper to keep the screen resizeable
def init_screen(width, height):
    global temp_surface
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    temp_surface = pygame.Surface((width / 2, height / 2)).convert()
    return screen


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    screen = init_screen(800, 600)
    pygame.display.set_caption('Quest - An epic journey.')

    try:
        game = Game()
        game.run()
    except:
        pygame.quit()
        raise
