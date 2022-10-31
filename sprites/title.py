from pico2d import *

class Title:
    def __init__(self):
        self.image = load_image('title_image.png')

    def draw(self):
        self.image.draw(400,300)
