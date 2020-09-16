import pygame
import sys
import time

from buttons import Button, PButtons, AIButton
from score import Score
from timer import Timer

class RockPaperScissors:
    """A class to manage the game."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((650, 400))
        pygame.display.set_caption("Rock-Paper-Scissors")

        # Make all fields.
        self._make_fields()



    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self._draw_fields()
        pygame.display.flip()

    def _make_fields(self):
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
        self.score = Score(self, "10")
        self.timer = Timer(self)

    def _draw_fields(self):
        """Draw all the fields."""
        self.r_button.draw_button()
        self.p_button.draw_button()
        self.s_button.draw_button()
        self.q_button.draw_button()
        self.ai_button.draw_button()
        self.score.draw_score()
        self._draw_time()

    def _draw_time(self):
        start_time = pygame.time.get_ticks()
        time = str(int(start_time / 1000))
        self.timer.show_time(time)
        self.timer.draw_timer()
