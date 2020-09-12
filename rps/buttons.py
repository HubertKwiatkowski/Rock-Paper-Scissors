import pygame.font

x = 0
y = 0

class Button():
    """A class to generate R-P-S buttons."""

    def __init__(self, rps_game, msg):
        """Initialize R-P-S button attributes."""
        self.screen = rps_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimentions and properties of buttons
        self.width, self.height = 100, 100
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 80)

        # Build the buttons rect object and put it in right top corner.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y

        # Store fields exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Prep button message.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
            )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class AIButton(Button):
    """A class to generate AI button."""

    def __init(self, rps_game, msg, width, height):
        """Initialize AI button atributes."""
        super().__init__()

        # set AI button parameters.
        self.width, self.height = 150, 150
        self.button.color = (0, 0, 255)
