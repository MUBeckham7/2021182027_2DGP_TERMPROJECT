from pico2d import *
import CharacterSelect_state

class PaulPheonix_Portrait:
    def __init__(self):
        self.image = load_image('paulpheonix_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 30, 31, 0, '',550,130,90,93)

        if CharacterSelect_state.x2 == -100:
            self.image.clip_composite_draw(0,0,30,31,0,'',600,450,30*5,31*5)