import pygame.font

class Score():
    """A class to display score."""

    def __init__(self, rps_game, msg):
        """Initialize score attributes."""
        self.screen = rps_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties.
        self.width, self.height = 150, 150
        self.score_color = (255, 0, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 100)

        # Build the buttons rect object and place it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 250
        self.rect.y = 50

        # Store score exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on score field."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.score_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_score(self):
        """Draw blank score field and then draw score."""
        self.screen.fill(self.score_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
