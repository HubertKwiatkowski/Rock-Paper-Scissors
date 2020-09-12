import pygame.font

class Button():
    """A class to generate buttons."""

    def __init__(self, rps_game):
        """Initialize button attributes."""
        self.screen = rps_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set properties of buttons
        self.text_color = (0, 0, 0)
        self.width, self.height = 100, 100

        # Build the buttons rect object and put it in right top corner.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 0
        self.rect.y = 0

        # Store buttons exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class PButtons(Button):
    """A class to generate Player buttons."""

    def __init__(self, rps_game):
        """Initialize Player buttons."""
        super().__init__(rps_game)

        # Set Player buttons properties.
        self.width, self.height = 100, 100
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 80)

class AIButton(Button):
    """A class to generate AI button."""

    def __init__(self, rps_game):
        """Initialize AI button atributes."""
        super().__init__(rps_game)

        # Set AI button properties.
        self.width, self.height = 150, 150
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 130)
