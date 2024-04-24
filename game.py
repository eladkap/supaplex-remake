import arcade
from settings import *


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        """
        Initilizes game window
        :param width: game window width
        :param height: game window height
        """
        super().__init__(width, height, title)
        arcade.set_background_color(COLORS['GRAY0'])
        self.width = width
        self.height = height
        self.title = title

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.width / 2, self.height / 2, RADIUS, COLORS['ORANGE'])

        # arcade.draw_text('🙂', self.width / 2, self.height / 2, COLORS['ORANGE'], font_size=14)
