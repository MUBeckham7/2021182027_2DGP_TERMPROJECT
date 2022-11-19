from pico2d import *
import game_state

class Win:
    def __init__(self):
        self.image = load_image('win.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_composite_draw(0, 0, 460, 50, 0, '', 346, 492, 15, 15)  # 카주야 1승
        # if game_state.jin_win_count >= 1:
        #     self.image.clip_composite_draw(0,0,460,50,0,'',346,492,15,15)       #진 1승
        # if game_state.jin_win_count >= 2:
        #     self.image.clip_composite_draw(0, 0, 460, 50, 0, '', 346, 492, 15, 15)  # 진 1승
        #     self.image.clip_composite_draw(0, 0, 460, 50, 0, '', 326, 492, 15, 15)  # 진 2승
        #
        # if game_state.kazuya_win_count >= 1:
        #     self.image.clip_composite_draw(0,0,460,50,0,'',346,492,15,15)       #카주야 1승
        # if game_state.kazuya_win_count >= 2:
        #     self.image.clip_composite_draw(0, 0, 460, 50, 0, '', 346, 492, 15, 15)  # 카주야 1승
        #     self.image.clip_composite_draw(0, 0, 460, 50, 0, '', 326, 492, 15, 15)  # 카주야 2승