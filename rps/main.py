import pygame
import sys
import time

from buttons import Button, PButtons, AIButton
from score import Score

class RockPaperScissors:
    """A class to manage the game."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((650, 400))
        pygame.display.set_caption("Rock-Paper-Scissors")

        # Make all fields.
        self._make_buttons()
        self._make_score()

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            self._update_screen()

    def timer(self):
        """Game timer"""
        for remaining in range(10, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2s} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rU lost")

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self._draw_fields()
        pygame.display.flip()

    def _make_buttons(self):
        """Make buttons for player and AI."""
        x = 50
        y = 250
        self.r_button = PButtons(self)
        self.r_button.rect.x = x
        self.r_button.rect.y = y
        self.r_button.prep_msg("R")
        self.p_button = PButtons(self)
        self.p_button.rect.x = x + 150
        self.p_button.rect.y = y
        self.p_button.prep_msg("P")
        self.s_button = PButtons(self)
        self.s_button.rect.x = x + 300
        self.s_button.rect.y = y
        self.s_button.prep_msg("S")
        self.q_button = PButtons(self)
        self.q_button.rect.x = x + 450
        self.q_button.rect.y = y
        self.q_button.prep_msg("Q")
        self.ai_button = AIButton(self)
        self.ai_button.rect.x = 450
        self.ai_button.rect.y = 50
        self.ai_button.prep_msg(":)")

    def _make_score(self):
        self.score = Score(self, "10")

    def _draw_fields(self):
        """Draw buttons."""
        self.r_button.draw_button()
        self.p_button.draw_button()
        self.s_button.draw_button()
        self.q_button.draw_button()
        self.ai_button.draw_button()
        self.score.draw_score()
