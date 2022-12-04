from pico2d import *

a=0
class RightLifeBar:
    def __init__(self):
        self.image = load_image('right_lifebar.png')

    def update(self):
        pass

    #기본 613,325
    def draw(self):
        global a
        self.image.clip_composite_draw(0,0,460,50,0,'',613-(0.9*a),515,325-(2*a),38)
        print('우 라이프 바:', a)
