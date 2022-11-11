from pico2d import *

class GameOver:
    def __init__(self):
        self.image = load_image('game_over.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,300)