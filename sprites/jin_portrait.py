from pico2d import *
import CharacterSelect_state

class JIN_Portrait:
    def __init__(self):
        self.image = load_image('jin_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 32, 31, 0, '',150,130,96,93)

        if CharacterSelect_state.x1 == 0:
            self.image.clip_composite_draw(0,0,32,31,0,'',200,450,32*5,31*5)