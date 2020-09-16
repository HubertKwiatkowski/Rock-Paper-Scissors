import pygame.font
import sys
import time

class Timer():
    """A class to generate game timer."""

    def __init__(self, rps_game, time):
        """Initialize Timer atributes."""
        self.screen = rps_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimentions and properties.
        self.width, self.height = 200, 150
        self.timer_color = (255, 0, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 70)

        # Build the timer object and place it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 50
        self.rect.y = 50



    def timer(self):
        """Game timer."""
        for remaining in range(10, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:10}".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rU lost")
