from pico2d import *
import rightlifebar

RD, LD, RU, LU, PU,PD, KU,KD = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'PU', 'KU','PD','KD']

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
        self.image.clip_draw((self.frame * 142) + 830, 2520, 120, 140, self.x, self.y)


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
        if self.dir == 0.1:
            self.image.clip_draw(-20, 250, 120, 140, self.x, self.y)
        if self.dir == -0.3:
            self.image.clip_draw((self.frame * 142) + 830, 2520, 120, 140, self.x, self.y)

class PUNCH:
    def enter(self, event):
        self.punch_1 = 1
        print('ENTER PUNCH')
    def exit(self, event):
        print('EXIT PUNCH')

    def do(self):
        self.punch_1 = (self.punch_1 + 1) % 3
        delay(0.1)
    def draw(self):
        self.image.clip_draw((self.punch_1) * 142+1120, 1000, 120, 140, self.x, self.y)
        draw_rectangle(self.x+10,self.y+15,self.x-20,self.y + 30)

class KICK:
    def enter(self, event):
        self.kick_1 = 3
        print('ENTER KICK')

    def exit(self, event):
        print('EXIT KICK')

    def do(self):
        self.kick_1 = (self.kick_1 + 1) % 4
        delay(0.1)

    def draw(self):
        self.image.clip_draw((self.kick_1) * 142-30,1000,120,140,self.x,self.y)
        draw_rectangle(self.x+10,self.y+5,self.x-25,self.y + 35)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN ,PD:PUNCH,PU:PUNCH,KD:KICK,KU:KICK},
    RUN: {RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE,PD:PUNCH,PU:PUNCH, KD:KICK,KU:KICK},
    PUNCH:{RU:PUNCH,LU:PUNCH,RD:PUNCH,LD:PUNCH,PU:IDLE,PD:IDLE,KU:PUNCH,KD:PUNCH},
    KICK:{RU:KICK,LU:KICK,RD:KICK,LD:KICK,PD:KICK,PU:KICK,KU:IDLE,KD:IDLE}
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
        rightlifebar.a += 1
        self.bgm = load_music('jin_punch_sound.mp3')
        self.bgm.set_volume(15)
        self.bgm.repeat_play()

