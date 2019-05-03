import pygame
from settings import Settings
from ship import Ship
import game_fuctions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    # start the main loop for the game
    while True:

        # redraw the screen during each pass though the loop
        screen.fill(ai_settings.bg_color)

        gf.check_events(ship)
        ship.update()
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()
