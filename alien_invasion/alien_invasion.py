import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    # ai_settings = Settings
    screen = pygame.display.set_mode(
        (Settings.screen_width, Settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(Settings.bg_color)

        pygame.display.flip()


run_game()
