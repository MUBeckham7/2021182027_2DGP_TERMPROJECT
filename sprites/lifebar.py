from pico2d import *

class LifeBar:
    def __init__(self):
        self.image = load_image('life bar.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,500)