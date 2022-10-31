from pico2d import *
Screen_width,Screen_Height = 1200,800

class BackGround:
    def __init__(self):
        self.image = load_image('BackGrounds1.png')

    def draw(self):
        self.image.draw(Screen_width // 2 + 1, Screen_Height // 2 + 1)