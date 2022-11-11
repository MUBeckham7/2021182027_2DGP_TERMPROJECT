from pico2d import *

class RightLifeBar:
    def __init__(self):
        self.image = load_image('right_lifebar.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0,0,460,50,0,'',613,515,325,38)