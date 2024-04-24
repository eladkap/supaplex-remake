import arcade
import dataclasses
from settings import *


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.set_background_color(arcade.color.ANTIQUE_WHITE)

    arcade.start_render()

    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE)

    arcade.finish_render()

    arcade.run()


if __name__ == '__main__':
    main()
