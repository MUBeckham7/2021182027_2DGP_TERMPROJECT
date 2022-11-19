from pico2d import *
import rightlifebar
import game_state

RD, LD, RU, LU, PU, PD, KU, KD = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'PU', 'KU', 'PD', 'KD']

key_event_table = {
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYDOWN, SDLK_KP_0): PU,
    (SDL_KEYDOWN, SDLK_KP_5): KU,
    (SDL_KEYUP, SDLK_KP_0): PD,
    (SDL_KEYUP, SDLK_KP_5): KD,
}

i=100
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 6

    @staticmethod
    def draw(self):
        global i
        #self.image.clip_draw(690, 2140, 120, 140, self.x, self.y)
        if game_state.k_hit == True:
            i -= 1
            self.image.clip_draw(690, 2140, 120, 140, self.x, self.y)
            print(i)
            if i == 0:
                i=100
                game_state.k_hit = False
        else:
            self.image.clip_draw((self.frame * 142) + 830, 2520, 120, 140, self.x, self.y)


ax=0
ay=0

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 0.1
        elif event == LD:
            self.dir -= 0.3
        elif event == RU:
            self.dir -= 0.1
        elif event == LU:
            self.dir += 0.3

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        global i
        if game_state.k_hit == True:
            i -= 1
            self.image.clip_draw(690, 2140, 120, 140, self.x, self.y)
            print(i)
            if i == 0:
                i=100
                game_state.k_hit = False
        else:
            if self.dir == 0.1:
                self.image.clip_draw(-20, 250, 120, 140, self.x, self.y)
            if self.dir == -0.3:
                self.image.clip_draw((self.frame * 142) + 830, 2520, 120, 140, self.x, self.y)


a = 0
b = 0


class PUNCH1:
    def __init__(self):
        self.x = 600
        self.y = 200

    def enter(self, event):
        self.punch_1 = 1
        print('ENTER PUNCH')

    def exit(self, event):
        global a, b
        a, b = 0, 0
        print('EXIT PUNCH')

    def do(self):
        self.punch_1 = (self.punch_1 + 1) % 3
        delay(0.1)

    def draw(self):
        global a, b
        global i
        if game_state.k_hit == True:
            i -= 1
            self.image.clip_draw(690, 2140, 120, 140, self.x, self.y)
            print(i)
            if i == 0:
                i = 100
                game_state.k_hit = False
        else:
            self.image.clip_draw((self.punch_1) * 142 + 1120, 1000, 120, 140, self.x, self.y)
            draw_rectangle(self.x + 10, self.y + 15, self.x - 20, self.y + 30)

        a = self.x
        b = self.y


    def get_bb(self):
        global i
        if i == 100:
            return a - 20, b + 30, a + 10, b + 15

        else:
            return 0,0,0,0
    def handle_collision(self,other, group):
        print('jin punched by kazuya')


class KICK1:
    def __init__(self):
        self.x = 600
        self.y = 200

    def enter(self, event):

        self.kick_1 = 3
        print('ENTER KICK')

    def exit(self, event):
        global a, b
        a, b = 0, 0
        print('EXIT KICK')

    def do(self):
        self.kick_1 = (self.kick_1 + 1) % 4
        delay(0.1)

    def draw(self):
        global a, b
        global i
        if game_state.k_hit == True:
            i -= 1
            self.image.clip_draw(690, 2140, 120, 140, self.x, self.y)
            print(i)
            if i == 0:
                i = 100
                game_state.k_hit = False
        else:
            self.image.clip_draw((self.kick_1) * 142 - 30, 1000, 120, 140, self.x, self.y)
            draw_rectangle(self.x + 10, self.y + 5, self.x - 25, self.y + 35)

        a = self.x
        b = self.y


    def get_bb(self):
        global i
        if i == 100:
            return  a +10, b + 5 , a -25, b + 35
        else:
            return 0,0,0,0

    def handle_collision(self, other, group):
        print('kazuya kickeed by jin')


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, PD: PUNCH1, PU: PUNCH1, KD: KICK1, KU: KICK1},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, PD: PUNCH1, PU: PUNCH1, KD: KICK1, KU: KICK1},
    PUNCH1: {RU: PUNCH1, LU: PUNCH1, RD: PUNCH1, LD: PUNCH1, PU: IDLE, PD: IDLE, KU: PUNCH1, KD: PUNCH1},
    KICK1: {RU: KICK1, LU: KICK1, RD: KICK1, LD: KICK1, PD: KICK1, PU: KICK1, KU: IDLE, KD: IDLE}
}


class Kazuya:

    def __init__(self):

        self.x, self.y = 600, 200
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('Kazuya_reverse.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}  Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x + 10, self.y - 55, self.x + 60, self.y + 50

    def handle_collision(self, other, group):
        rightlifebar.a += 5
        self.bgm = load_music('jin_punch_sound.mp3')
        self.bgm.set_volume(15)
        self.bgm.play()


