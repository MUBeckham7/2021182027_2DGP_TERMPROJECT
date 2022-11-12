from pico2d import *
import leftlifebar

RD, LD, RU, LU, PU,PD, KU,KD = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'PU', 'KU','PD','KD']

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYDOWN, SDLK_SPACE): PU,
    (SDL_KEYDOWN, SDLK_k): KU,
    (SDL_KEYUP, SDLK_SPACE): PD,
    (SDL_KEYUP, SDLK_k): KD,
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
        self.frame = (self.frame + 1) % 4

    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame * 160, 2580, 100, 140, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 0.3
        elif event == LD:
            self.dir -= 0.1
        elif event == RU:
            self.dir -= 0.3
        elif event == LU:
            self.dir += 0.1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == 0.3:
            self.image.clip_draw(self.frame * 160, 2580, 100, 140, self.x, self.y)
        if self.dir == -0.1:
            self.image.clip_draw(640, 80, 130, 100, self.x, self.y)

class PUNCH:
    def enter(self, event):
        self.punch_1 = 3
        print('ENTER PUNCH')
    def exit(self, event):
        print('EXIT PUNCH')

    def do(self):
        self.punch_1 = (self.punch_1 + 1) % 4
        delay(0.1)
        pass
    def draw(self):
        self.image.clip_draw((self.punch_1) * 170, 1220, 115, 140, self.x, self.y)

class KICK:
    def enter(self, event):
        self.kick_1 = 2
        print('ENTER KICK')

    def exit(self, event):
        print('EXIT KICK')

    def do(self):
        self.kick_1 = (self.kick_1 + 1) % 5
        delay(0.1)

    def draw(self):
        self.image.clip_draw((self.kick_1 * 170 )+ 630, 1220, 130, 160, self.x, self.y)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN ,PD:PUNCH,PU:PUNCH,KD:KICK,KU:KICK},
    RUN: {RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE,PD:PUNCH,PU:PUNCH, KD:KICK,KU:KICK},
    PUNCH:{RU:PUNCH,LU:PUNCH,RD:PUNCH,LD:PUNCH,PU:IDLE,PD:IDLE,KU:PUNCH,KD:PUNCH},
    KICK:{RU:KICK,LU:KICK,RD:KICK,LD:KICK,PD:KICK,PU:KICK,KU:IDLE,KD:IDLE}
}


class Jin:

    def __init__(self):
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('Jin.png')

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
        return self.x - 10, self.y - 55, self.x + 40, self.y + 40

    def handle_collision(self, other, group):
        print('boy meet ball')
        leftlifebar.a += 1
        delay(0.3)


