from pico2d import *

class Haeiachi_Portrait:
    def __init__(self):
        self.image = load_image('haeiachi_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 30, 30, 0, '',250,130,90,90)