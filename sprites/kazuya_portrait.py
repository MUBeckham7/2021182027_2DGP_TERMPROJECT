from pico2d import *
import CharacterSelect_state

class Kazuya_Portrait:
    def __init__(self):
        self.image = load_image('kazuya_portrait.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 32, 29, 0, '',650,130,96,87)

        if CharacterSelect_state.x2 == 0:
            self.image.clip_composite_draw(0,0,32,29,0,'',600,450,32*5,29*5)