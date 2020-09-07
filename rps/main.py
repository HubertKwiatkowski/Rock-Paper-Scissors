import pygame
import sys

class RockPaperScissors:
    """A class to manage the game."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((650, 400))
        pygame.display.set_caption("Rock-Paper-Scissors")

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
