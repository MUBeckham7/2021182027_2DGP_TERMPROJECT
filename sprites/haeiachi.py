from pico2d import *
import leftlifebar
import game_state
import rightlifebar

RD, LD, RU, LU, PU, PD, KU, KD = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'PU', 'KU', 'PD', 'KD']

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYDOWN, SDLK_SPACE): PU,
    (SDL_KEYDOWN, SDLK_b): KU,
    (SDL_KEYUP, SDLK_SPACE): PD,
    (SDL_KEYUP, SDLK_b): KD,
}

defence = False
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
        self.frame = (self.frame+1) % 2
        self.fra = (self.fra+1) % 2

    @staticmethod
    def draw(self):
        global i
        if game_state.h_hit == True:
            i -= 1
            self.image.clip_draw(72, 260, 80, 100, self.x+5, self.y)
            if i == 0:
                i=100
                game_state.h_hit = False
        elif leftlifebar.a >= 164:
            if game_state.i>500:
                self.image.clip_draw(0, 160, 100, 100, self.x + 5, self.y)
            if game_state.i<500 and game_state.i>0:
                self.image.clip_draw(220, 190, 130, 60, self.x - 5, self.y - 10)
        else:
            self.image.clip_draw(self.frame * 72, 1200, 64, 110, self.x+5, self.y-15)
            #self.image.clip_composite_draw(-10, 0, 65 , 90,0,'', self.x, self.y,70,100)


class RUN:
    def enter(self, event):
        global defence
        print('ENTER RUN')
        if event == RD:
            self.dir += 0.3
        elif event == LD:
            self.dir -= 0.1
            defence = True
        elif event == RU:
            self.dir -= 0.3
        elif event == LU:
            self.dir += 0.1

    def exit(self, event):
        global defence
        defence = False
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        global i
        if game_state.h_hit == True:
            if defence == True:
                self.image.clip_composite_draw(-10, 0, 65, 90, 0, '', self.x, self.y, 70, 100)
                game_state.h_hit=False
            else:
                i -= 1
                self.image.clip_draw(72, 260, 80, 100, self.x+5, self.y)
                if i == 0:
                    i = 100
                    game_state.h_hit = False
        else:
            print(self.dir)
            if self.dir == 0.3:
                self.image.clip_draw(self.frame * 72, 1200, 64, 110, self.x + 5, self.y - 15)
            if self.dir == -0.1:
                self.image.clip_composite_draw(-10, 0, 65, 90, 0, '', self.x, self.y, 70, 100)



a = 0
b = 0


class PUNCH3:
    def __init__(self):
        self.x = 200
        self.y = 200


    def enter(self, event):
        self.punch_1 = 1
        print('ENTER PUNCH')

    def exit(self, event):
        global a,b
        a,b=0,0
        print('EXIT PUNCH')

    def do(self):
        self.punch_1 = (self.punch_1 + 1) % 4
        delay(0.1)

    def draw(self):
        global a,b
        global i
        if game_state.h_hit == True:
            i -= 1
            self.image.clip_draw(72, 260, 80, 100, self.x+5, self.y)
            if i == 0:
                i = 100
                game_state.h_hit = False
        else:
            self.image.clip_draw((self.punch_1 * 80 )+259, 1110, 80, 97, self.x+20, self.y)
            #draw_rectangle(self.x + 30, self.y+3, self.x + 60, self.y + 18)
        a = self.x + 30
        b = self.y + 3


    def get_bb(self):
        global i
        if i == 100:
            return a,b,a+30,b+15
        else:
            return 0,0,0,0

    def handle_collision(self, other, group):
        print('kazuya punched by jin')


class KICK3:
    def __init__(self):
        self.x = 200
        self.y = 200

    def enter(self, event):
        self.kick_1 = 2
        print('ENTER KICK')

    def exit(self, event):
        global a, b
        a, b = 0, 0
        print('EXIT KICK')

    def do(self):
        self.kick_1 = (self.kick_1 + 1) % 3
        delay(0.1)

    def draw(self):
        global a,b
        global i
        if game_state.h_hit == True:
            i -= 1
            self.image.clip_draw(72, 260, 80, 100, self.x+5, self.y)
            if i == 0:
                i = 100
                game_state.h_hit = False
        else:
            self.image.clip_draw(self.kick_1 * 100,730 , 137, 90, self.x+10, self.y-3)
            #draw_rectangle(self.x+40,self.y+10,self.x + 75,self.y + 30)
        a = self.x + 35
        b = self.y + 10

    def get_bb(self):
        global i
        if i == 100:
            return a ,b,a+35,b+20
        else:
            return 0,0,0,0

    def handle_collision(self, other, group):
        print('kazuya kicked by jin')

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, PD: PUNCH3, PU: PUNCH3, KD: KICK3, KU: KICK3},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, PD: PUNCH3, PU: PUNCH3, KD: KICK3, KU: KICK3},
    PUNCH3: {RU: PUNCH3, LU: PUNCH3, RD: PUNCH3, LD: PUNCH3, PU: IDLE, PD: IDLE, KU: PUNCH3, KD: PUNCH3},
    KICK3: {RU: KICK3, LU: KICK3, RD: KICK3, LD: KICK3, PD: KICK3, PU: KICK3, KU: IDLE, KD: IDLE}
}


class Haeiachi:

    def __init__(self):
        self.x, self.y = 200, 200
        self.frame = 0
        self.fra= 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('Haeiachi.png')

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
        #draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 20, self.y - 55, self.x + 40, self.y + 40

    def handle_collision(self, other, group):
        if defence == False:
            leftlifebar.a += 5
        self.bgm = load_music('kazuya_punch_sound.mp3')
        self.bgm.set_volume(15)
        self.bgm.play()