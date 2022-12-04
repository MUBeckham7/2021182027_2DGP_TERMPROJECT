from pico2d import *
import game_state
import game_world

a = 0


class LeftLifeBar:
    def __init__(self):
        self.image = load_image('left_lifebar.png')

    def update(self):
        pass

    def draw(self):
        global a
        self.image.clip_composite_draw(0, 0, 460, 50, 0, '', 185 + (0.9 * a), 510, 325 - (2 * a), 40)

        #if a == 164:
            #game_world.add_object(game_state.gameover, 1)
