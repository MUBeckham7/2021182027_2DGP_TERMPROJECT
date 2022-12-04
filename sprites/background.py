from pico2d import *
Screen_width,Screen_Height = 1200,800

class BackGround:
    def __init__(self):
        self.image = load_image('BackGrounds1.png')
        self.bgm = load_wav('game_state_sound.mp3')
        self.bgm.set_volume(15)
        self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(Screen_width // 2 + 1, Screen_Height // 2 + 1)

    def get_bb(self):
        return 0,0,800,600

