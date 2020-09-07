import pygame

class RockPaperScissors:
    """A class to manage the game."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.setmode((650, 400))
        pygame.display.set_caption("Rock-Paper-Scissors")
