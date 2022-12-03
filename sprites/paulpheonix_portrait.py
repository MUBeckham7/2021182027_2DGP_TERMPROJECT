from pico2d import *

class PaulPheonix_Portrait:
    def __init__(self):
        self.image = load_image('paulpheonix_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 30, 31, 0, '',550,130,90,93)