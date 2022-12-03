from pico2d import *

class JIN_Portrait:
    def __init__(self):
        self.image = load_image('jin_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 32, 31, 0, '',150,130,96,93)