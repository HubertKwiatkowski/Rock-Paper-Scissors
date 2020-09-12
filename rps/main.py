import pygame
import sys

from buttons import Button, AIButton

class RockPaperScissors:
    """A class to manage the game."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((650, 400))
        pygame.display.set_caption("Rock-Paper-Scissors")

        # Make and draw buttons.
        self._make_buttons()



    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self._draw_buttons()
        pygame.display.flip()

    def _make_buttons(self):
        """Make buttons for player and AI."""
        self.r_button.x = 50
        y = 250
        self.r_button = Button(self, "R")
        # self.r_button.rect.x = x
        # self.r_button.rect.y = y
        self.p_button = Button(self, "P")
        self.p_button.rect.x = x + 150
        self.p_button.rect.y = y
        self.s_button = Button(self, "S")
        self.s_button.rect.x = x + 300
        self.s_button.rect.y = y
        self.q_button = Button(self, "Q")
        self.q_button.rect.x = x + 450
        self.q_button.rect.y = y
        self.ai_button = AIButton(self, ":)")
        self.ai_button.rect.x = 450
        self.ai_button.rect.y = 50

    def _draw_buttons(self):
        """Draw buttons."""
        self.r_button.draw_button()
        self.p_button.draw_button()
        self.s_button.draw_button()
        self.q_button.draw_button()
        self.ai_button.draw_button()
