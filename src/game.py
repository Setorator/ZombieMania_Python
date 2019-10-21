import sys
import pygame as pg
import pyscroll
from pytmx.util_pygame import load_pygame

from zombiemania.src.zombie import Zombie

class Game:

    def __init__(self):
        # Init pygame
        pg.init()
        pg.font.init()
        window = width, height = 800, 600
        self.screen = pg.display.set_mode(window, pg.RESIZABLE)
        self.tmp_surface = pg.Surface(window).convert()
        pg.display.set_caption("Zombie Mania - It's just a flesh wound!")

        # Load data from TMX-map
        self.map_path = "../res/maps/map0.tmx"
        tmx_data = load_pygame(self.map_path)
        map_data = pyscroll.data.TiledMapData(tmx_data)

        # Create renderer (camera)
        # clamp_camera is used to prevent the map from scrolling past the edge
        # TODO: Fix so that the renderer doesn't render the whole screen, only the visible
        self.map_layer = pyscroll.BufferedRenderer(map_data,
                                                   window,
                                                   clamp_camera=True)

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)
        self.zombie = Zombie()
        self.group.add(self.zombie)

    def draw(self, surface):
        self.group.center(self.zombie.rect.center)
        self.group.draw(surface)

    def run(self):
        scale = pg.transform.scale

        try:
            # Update the surface and display on the screen
            self.draw(self.tmp_surface)
            scale(self.tmp_surface, self.screen.get_size(), self.screen)
            pg.display.flip()
        except:
            pg.quit()


def main():
    # Game parameters
    game = Game()

    # Main loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        game.run()

        """
            # TODO: fix collision handling
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    if zombie.rect.right + zombie.velocity[0] <= width:
                        zombie.velocity = (v_x, None)
                    else:
                        print("Out of right border!")

            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    zombie.velocity = (0, None)

        # Refresh image
        window.fill(black)
        """
        # Update map
        """
        for row in range(game_map.map_height):
            for column in range(game_map.map_width):
                x_pos = column * game_map.tile_size
                y_pos = row * game_map.tile_size
                tile = game_map.current_level[row][column]
                if tile is not None:
                    rect = pg.Rect(x_pos, y_pos, game_map.tile_size, game_map.tile_size)
                    window.blit(tile, rect)
        """

if __name__ == '__main__':
    main()
