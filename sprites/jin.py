from pico2d import *

RD, LD, RU, LU, PUNCH_D, KICK_D,PUNCH_U,KICK_U = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'PUNCH', 'KICK']

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYDOWN, SDLK_SPACE): PUNCH_D,
    (SDL_KEYDOWN, SDLK_k): KICK_D,
    (SDL_KEYUP, SDLK_SPACE): PUNCH_U,
    (SDL_KEYUP, SDLK_k): KICK_U,
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
            self.dir += 1
        elif event == LD:
            self.dir -= 0.1
        elif event == RU:
            self.dir -= 1
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
        if self.dir == 1:
            self.image.clip_draw(self.frame * 160, 2580, 100, 140, self.x, self.y)
        if self.dir == -0.1:
            self.image.clip_draw(640, 80, 130, 100, self.x, self.y)

class Jin_Punch:
    def enter(self, event):
        pass
    def exit(self, event):
        pass
    def do(self):
        self.frame = (self.frame + 1) % 4
        pass
    def draw(self):
        self.image.clip_draw(self.frame * 160, 2580, 100, 140, self.x, self.y)
        pass
class Jin_Kick:
    def enter(self, event):
        pass
    def exit(self, event):
        pass

    def do(self):
        pass

    def draw(self):
        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN , PUNCH_D:Jin_Punch,PUNCH_U:Jin_Punch, KICK_D:Jin_Kick,KICK_U:Jin_Kick},
    RUN: {RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE,PUNCH_D:Jin_Punch,PUNCH_U:Jin_Punch, KICK_D:Jin_Kick,KICK_U:Jin_Kick},
    Jin_Punch:{RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE},
    Jin_Kick:{RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE}
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
        return self.x - 10, self.y - 55, self.x + 30, self.y + 40

    def handle_collision(self, other, group):
        print('boy meet ball')


