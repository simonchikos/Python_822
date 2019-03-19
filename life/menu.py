import pygame
import field
import button


class Menu:
    """В Menu опишем 3 кнопки start, restart, quit"""

    FONT = 'calibri'
    FONT_SIZE = 36

    def __init__(self, game_f):
        self.start = button.Button(
            'start',
            Menu.FONT,
            Menu.FONT_SIZE,
            0,
            game_f.field_size[1] - field.Field.menu_height
        )

        self.restart = button.Button(
            'restart',
            Menu.FONT,
            Menu.FONT_SIZE,
            button.Button.widht + button.Button.margin,
            game_f.field_size[1] - field.Field.menu_height
        )

        self.quit = button.Button(
            'quit',
            Menu.FONT,
            Menu.FONT_SIZE,
            (button.Button.widht + button.Button.margin) * 2,
            game_f.field_size[1] - field.Field.menu_height
        )

    def draw(self, surface):
        for but in (self.start, self.restart, self.quit):
            but.draw(surface)

    def click(self, pos, state):
        if pos[0] < button.Button.widht and state == 'draw':
            return 'evolution'
        elif button.Button.widht < pos[0] < button.Button.widht * 2 + button.Button.margin:
            return 'restart'
        elif (
                button.Button.widht * 2 + button.Button.margin <
                pos[0] <
                button.Button.widht * 3 + button.Button.margin * 2
        ):
            return 'quit'
        return state
