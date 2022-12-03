from pico2d import *

class Kazuya_Portrait:
    def __init__(self):
        self.image = load_image('kazuya_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 32, 29, 0, '',650,130,96,87)