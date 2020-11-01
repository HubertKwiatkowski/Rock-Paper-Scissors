import pygame
import sys
import time
import random

from buttons import Button, PButtons, AIButton
from score import Score
from timer import Timer

restart_time = 0
sc = 0
WIDTH, HEIGHT = 650, 400

class RockPaperScissors:
    """A class to manage the game."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Rock-Paper-Scissors")
        self._start()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    l, x, y, visible = button
                    if (x < mouse_pos[0] < x + 100) and (y < mouse_pos[1] < y + 100):
                        if button[0] == 'Q':
                            sys.exit()
                        else:
                            button[3] = False
                            player_choice = button[0]
                            ai_choice = random.choice(['R', 'P', 'S'])
                            global sc
                            score = self._compare(player_choice, ai_choice)
                            sc += score
                            self._draw_chosen(ai_choice)

    def _update_screen(self):
        self._draw_all()
        pygame.display.flip()

    def _start(self):
        """Start parameters."""
        LETTERS = ['R', 'P', 'S', 'Q']
        global buttons
        buttons = []
        x = 50
        y = 250
        for l in LETTERS:
            buttons.append([l, x, y, True])
            x += 150

    def _draw_all(self):
        """Draw the window."""
        self._start()
        self.screen.fill((0, 0, 0))
        self._draw_player_fields()
        self._draw_ai(':)')
        self._draw_time()
        self._draw_score(sc)

    def _draw_chosen(self, ai_choice):
        """Draw window after choosing one of player's fields."""
        self.screen.fill((0, 0, 0))
        self._draw_chosen_field()
        self._draw_ai(ai_choice)
        self._draw_time()
        self._draw_score(sc)
        pygame.display.flip()
        pygame.time.delay(1500)
        global restart_time
        restart_time = pygame.time.get_ticks()

    def _draw_player_fields(self):
        """Draw all player fields."""
        global buttons
        for button in buttons:
            l, x, y, visible = button
            if visible:
                self.button = PButtons(self)
                self.button.rect.x = x
                self.button.rect.y = y
                self.button.prep_msg(l)
                self.button.draw_button()

    def _draw_chosen_field(self):
        """Draw chosen field."""
        global buttons
        for button in buttons:
            l, x, y, not_chosen = button
            if not not_chosen:
                self.button = PButtons(self)
                self.button.rect.x = x
                self.button.rect.y = y
                self.button.prep_msg(l)
                self.button.draw_button()

    def _draw_time(self):
        """Draw timer."""
        self.timer = Timer(self)
        global restart_time
        current_time = pygame.time.get_ticks()
        time = int((current_time - restart_time) / 1000)
        if time > 10: restart_time = pygame.time.get_ticks()
        self.timer.show_time(str(10 - time))
        self.timer.draw_timer()

    def _draw_ai(self, sign):
        self.ai_button = AIButton(self)
        self.ai_button.rect.x = 450
        self.ai_button.rect.y = 50
        self.ai_button.prep_msg(sign)
        self.ai_button.draw_button()

    def _draw_score(self, score):
        self.score = Score(self, str(sc))
        self.score.draw_score()

    def _compare(self, player_choice, ai_choice):
        """Compare player and AI coice."""
        if player_choice == 'R' and ai_choice == 'P':
            result = -1
        elif player_choice == 'R' and ai_choice == 'S':
            result = 1
        elif player_choice == 'P' and ai_choice == 'S':
            result = -1
        elif player_choice == 'P' and ai_choice == 'R':
            result = 1
        elif player_choice == 'S' and ai_choice == 'R':
            result = -1
        elif player_choice == 'S' and ai_choice == 'P':
            result = 1
        else:
            result = 0

        return result
