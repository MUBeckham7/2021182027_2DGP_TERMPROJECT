from pico2d import *

class Character_select:
    def __init__(self):
        self.image = load_image('character_select_background.png')
        #self.bgm = load_music('title_state_sound.mp3')
        #self.bgm.set_volume(30)
        #self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 507, 247, 0, '',400,300,800,600)