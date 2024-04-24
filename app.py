import arcade

from settings import *
from game import Game

if __name__ == '__main__':
    app = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Supaplex')
    arcade.run()
