import pygame
from assets.constants import WHITE, BLACK, FAMILY_FONT_NAME


def draw_text(surf, msg, size, color, x_text, y_text):
    """ Function to make easyer to draw text
    surf: pygame screen buffer (Where the text is going to be displayed)
    msg: string of what you want to say
    color: text color
    x_text: x position of your text
    y_text: y position of your text
    """
    font_name = pygame.font.match_font(FAMILY_FONT_NAME)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(
        msg, True, color
    )
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x_text, y_text)
    surf.blit(text_surface, text_rect)


class Basic_button:
    def __init__(self, msg, pos, size, iddle_color, active_color, action):
        """Initialization of the basic button
        msg: String with what you want the button to display
        pos: tupple (x,y) of the button's position
        size: tupple (w,h) of the button's size
        iddle_color: button's color when is not active
        active_color: button's color when is hovered
        """

        self.msg = msg
        self.pos = pos
        self.size = size
        self.iddle_color = iddle_color
        self.active_color = active_color
        self.color = iddle_color
        self.action = action

    def do_action(self):
        mouse = pygame.mouse.get_pos()
        if (self.pos[0] + self.size[0]) > mouse[0] > self.pos[0] and (self.pos[1] + self.size[1]) > mouse[1] > self.pos[1]:
            self.action()

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()

        if (self.pos[0] + self.size[0]) > mouse[0] > self.pos[0] and (self.pos[1] + self.size[1]) > mouse[1] > self.pos[1]:
            self.color = self.active_color
        else:
            self.color = self.iddle_color

        pygame.draw.rect(screen, self.color,
                         (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        draw_text(screen, self.msg, 20, WHITE,
                  self.pos[0]+self.size[0]/2, self.pos[1]+self.size[1]/2)


class Basic_car:
    def __init__(self, pos, size, speed, image):
        """
        TODO: ADD docstring
        """
        self.score = 0
        self.pos = pos
        self.speed = speed
        self.size = size
        self.image = image

    def collision(self, other):
        if (
            self.pos[0] < (other.pos[0]+other.size[0]) and
            (self.pos[0]+self.size[0]) > other.pos[0] and
            self.pos[1] < (other.pos[1]+other.size[1]) and
            (self.pos[1]+self.size[1]) > other.pos[1]
        ):
            return False
        return True

    def draw_score(self, screen):
        draw_text(
            screen,
            f"Dodged: {self.score}",
            25, BLACK,
            50,
            0
        )

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def move(self):
        self.pos = [self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]]


class Basic_grass:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [
            self.pos[0], self.pos[1], self.size[0], self.size[1]
        ]
        )
