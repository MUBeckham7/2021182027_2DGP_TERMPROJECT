from pico2d import *

a=0

class LeftLifeBar:
    def __init__(self):
        self.image = load_image('left_lifebar.png')

    def update(self):
        pass

    def draw(self):
        global a
        self.image.clip_composite_draw(0+a,0,460,50,0,'',185,510,325,40)