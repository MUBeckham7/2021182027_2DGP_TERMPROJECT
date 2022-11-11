from pico2d import *

class RightLifeBar:
    def __init__(self):
        self.image = load_image('right_lifebar.png')

    def update(self):
        pass

    #기본 613,325
    def draw(self):
        self.image.clip_draw_to_origin(0,0,460,50,613,515,100,80)
        self.image.clip_composite_draw(0,0,460,50,0,'',613,515,325,38)
