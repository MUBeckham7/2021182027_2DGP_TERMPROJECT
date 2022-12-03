from pico2d import *

class Character_select:
    def __init__(self):
        self.image = load_image('character_select_background.png')
        #self.bgm = load_music('title_state_sound.mp3')
        #self.bgm.set_volume(30)
        #self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400,300)