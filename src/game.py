import sys
import pygame as pg
import pyscroll
from pytmx.util_pygame import load_pygame

from zombiemania.settings import load_images
from zombiemania.src.zombie import Zombie


class Game:

    def __init__(self):
        # Init game parameters
        pg.init()
        pg.font.init()
        window = width, height = 800, 600
        self.screen = pg.display.set_mode(window, pg.RESIZABLE)
        self.tmp_surface = pg.Surface(window).convert()
        pg.display.set_caption("Zombie Mania - It's just a flesh wound!")

        self.background = load_images("BACKGROUND")

        # Load data from TMX-map
        self.map_path = "../res/maps/map0.tmx"
        tmx_data = load_pygame(self.map_path)
        self.meta_objects = tmx_data.visible_layers
        self.map_data = pyscroll.data.TiledMapData(tmx_data)

        # Create renderer (camera)
        # clamp_camera is used to prevent the map from scrolling past the edge
        # TODO: Fix so that the renderer doesn't render the whole screen, only the visible
        self.map_layer = pyscroll.BufferedRenderer(self.map_data,
                                                   (width, height),
                                                   clamp_camera=True,
                                                   alpha=True)

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)
        self.zombie = Zombie()
        self.group.add(self.zombie)

    def draw(self, surface):
        """
        Used to redraw all the objects in the game, including
        map, zombie and enemies
        :param surface: The surface on which to redraw the objects
        """

        # Render first background image then rotate the background animation
        pg.transform.scale(self.background[0], surface.get_size(), surface)
        self.background = self.background[1:] + self.background[:1]

        self.group.center(self.zombie.rect.center)
        self.group.draw(surface)

    def run(self):
        """
        Updates the system 1 tick by updating objects positions and
        redrawing them.
        """

        scale = pg.transform.scale
        try:
            # Update the surface and display on the screen
            self.group.update()
            self.draw(self.tmp_surface)
            scale(self.tmp_surface, self.screen.get_size(), self.screen)
            pg.display.flip()
        except:
            pg.quit()


def main():

    # Game parameters
    game = Game()

    # Main loop which should create a clock used for the game-ticks
    # TODO: fix a clock for updating the game with a fixed frequency
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # TODO: Move collision handling to the update() of the Game-class.
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    game.zombie.velocity = (2, None)

            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    game.zombie.velocity = (0, None)

        game.run()


if __name__ == '__main__':
    main()
