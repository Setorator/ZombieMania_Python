import sys
import pygame as pg
import pyscroll
from pytmx.util_pygame import load_pygame

from zombiemania.settings import load_images, BLOCK_SIZE
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
        self.meta_objects = tmx_data.visible_layers  # TODO: Needed?
        self.map_data = pyscroll.data.TiledMapData(tmx_data)

        # Add static obstacles to a dict for easy collision checking
        self.obstacles = []
        for obs in tmx_data.get_layer_by_name("Map"):
            if obs[2] != 0:
                pos = (obs[0] * BLOCK_SIZE, obs[1] * BLOCK_SIZE)
                tmp_rect = pg.Rect(pos, (BLOCK_SIZE, BLOCK_SIZE))
                self.obstacles.append(tmp_rect)

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

    def collisions(self):
        for sprite in self.group.sprites():
            if sprite.hitbox.collidelist(self.obstacles) > -1:
                sprite.move_back()

    def run(self):
        """
        Updates the system 1 tick by updating objects positions and redrawing
        them.
        """
        scale = pg.transform.scale
        try:
            # Update the surface and display on the screen
            self.group.update()
            self.collisions()
            self.draw(self.tmp_surface)
            scale(self.tmp_surface, self.screen.get_size(), self.screen)
            pg.display.flip()

        except:
            pg.quit()


def main():

    # Game parameters
    game = Game()
    clock = pg.time.Clock()

    # Main loop which should create a clock used for the game-ticks
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    game.zombie.velocity = (10, None)
                elif event.key == pg.K_LEFT:
                    game.zombie.velocity = (-10, None)
                elif event.key == pg.K_UP:
                    game.zombie.velocity = (None, -10)
                elif event.key == pg.K_DOWN:
                    game.zombie.velocity = (None, 10)

            # TODO: Improve movements (order: L_DOWN - R_DOWN - L_UP makes the zombie stop)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    game.zombie.velocity = (0, None)
                elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                    game.zombie.velocity = (None, 0)

        game.run()
        clock.tick(30)


if __name__ == '__main__':
    main()
