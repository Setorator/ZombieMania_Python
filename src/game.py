import zombiemania.settings as settings
import sys
import pygame as pg
from zombiemania.src.zombie import Zombie
from zombiemania.src.map_builder.map import Map


def main():
    # Game parameters
    window_size = width, height = 640, 480
    velocity = v_x, v_y = [2, 2]
    black = 0, 0, 0

    # Init map
    maps = Map()
    empty_tile = "t"

    # Init game
    pg.init()
    window = pg.display.set_mode(window_size)

    # Init objects
    zombie = Zombie()
    player_group = pg.sprite.Group(zombie)
    player_group.update()
    player_group.draw(window)
    pg.display.flip()

    # TODO: make this a test, where it's checked that the zombie is here
    player_group.__repr__()

    # Main loop
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

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
        # Update map

        for row in range(maps.map_height):
            for column in range(maps.map_width):
                x_pos = column*maps.tile_size
                y_pos = row*maps.tile_size
                tile = maps.current_level[row][column]
                if tile is not None:
                    rect = pg.Rect(x_pos, y_pos, maps.tile_size, maps.tile_size)
                    window.blit(tile, rect)

        player_group.update()
        player_group.draw(window)
        pg.display.flip()


if __name__ == '__main__':
    main()
