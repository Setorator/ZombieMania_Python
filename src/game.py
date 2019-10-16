import sys
import pygame
from zombiemania.src.zombie import Zombie


def main():
    # Game parameters
    window_size = width, height = 640, 480
    velocity = v_x, v_y = [2, 2]
    black = 0, 0, 0

    # Init game
    pygame.init()
    window = pygame.display.set_mode(window_size)

    # Init objects
    zombie = Zombie()
    player_group = pygame.sprite.Group(zombie)

    # TODO: make this a test, where it's checked that the zombie is here
    player_group.__repr__()

    # Main loop
    while True:

        for event in pygame.event.get():
            print(event.__repr__())
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # TODO: fix collision handling
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if zombie.rect.right + zombie.velocity[0] <= width:
                        zombie.velocity = (v_x, None)
                    else:
                        print("Out of right border!")

            elif event.type == pygame.KEYUP:
                print("KEYUP")
                if event.key == pygame.K_RIGHT:
                    print("KEYR")
                    zombie.velocity = (0, None)

        window.fill(black)
        player_group.update()
        player_group.draw(window)
        pygame.display.flip()


if __name__ == '__main__':
    main()
