from pico2d import *
import leftlifebar
import game_state
import rightlifebar

RD, LD, RU, LU, PU, PD, KU, KD = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'PU', 'KU', 'PD', 'KD']

key_event_table = {
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYDOWN, SDLK_o): PU,
    (SDL_KEYDOWN, SDLK_p): KU,
    (SDL_KEYUP, SDLK_o): PD,
    (SDL_KEYUP, SDLK_p): KD,
}

defence = False
i=100
k=0
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self, event):
        global k
        k=0
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        global k
        k+=1
        if k == 100:
            self.frame = (self.frame + 1) % 3
        self.fra = (self.fra+1) % 2

    @staticmethod
    def draw(self):
        global i,k
        if game_state.p_hit == True:
            i -= 1
            self.image.clip_composite_draw(217, 675, 90, 140,0,'', self.x+5, self.y,80,170)
            if i == 0:
                i=100
                game_state.p_hit = False
        elif rightlifebar.a >= 164:
            if game_state.i>500:
                self.image.clip_composite_draw(0, 220, 90, 110, 0, 'h', self.x + 10, self.y-20, 80, 110)
            if game_state.i<500 and game_state.i>0:
                self.image.clip_composite_draw(0, 170, 150, 60, 0, 'h', self.x + 20, self.y - 40, 150, 70)
        else:
            self.image.clip_composite_draw((self.frame * 76), 1657, 75, 100,0,'h', self.x, self.y,70,110)



class RUN:
    def enter(self, event):
        global defence
        print('ENTER RUN')
        if event == LD:
            self.dir -= 0.3
        elif event == RD:
            self.dir += 0.1
            defence = True
        elif event == LU:
            self.dir += 0.3
        elif event == RU:
            self.dir -= 0.1

    def exit(self, event):
        global k,defence
        k=0
        defence = False
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        global k
        k+=1
        if k == 100:
            self.frame = (self.frame + 1) % 3
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        global i,k
        if game_state.p_hit == True:
            if defence == True:
                self.image.clip_composite_draw(0, 320, 80, 100, 0, 'h', self.x + 10, self.y - 5, 80, 100)
                game_state.p_hit = False
            else:
                i -= 1
                self.image.clip_composite_draw(217, 675, 90, 140,0,'', self.x+5, self.y,80,170)
                if i == 0:
                    i = 100
                    game_state.p_hit = False
        else:
            if self.dir == -0.3:
                self.image.clip_composite_draw((self.frame * 76), 1657, 75, 100, 0, 'h', self.x, self.y, 70, 110)
            if self.dir == 0.1:
                self.image.clip_composite_draw(0, 320, 80, 100, 0, 'h', self.x + 10, self.y - 5, 80, 100)

a = 0
b = 0


class PUNCH2:
    def __init__(self):
        self.x = 600
        self.y = 200


    def enter(self, event):
        self.punch_1 = 1
        print('ENTER PUNCH')

    def exit(self, event):
        global a,b
        a,b=0,0
        print('EXIT PUNCH')

    def do(self):
        self.punch_1 = (self.punch_1 + 1) % 3
        delay(0.1)

    def draw(self):
        global a,b
        global i
        if game_state.p_hit == True:
            i -= 1
            self.image.clip_composite_draw(217, 675, 90, 140,0,'', self.x+5, self.y,80,170)
            if i == 0:
                i = 100
                game_state.p_hit = False
        else:
            self.image.clip_composite_draw((self.punch_1)*160, 1280, 80, 90, 0, 'h', self.x-10, self.y, 80, 100)
            #self.image.clip_draw((self.punch_1) * 170, 1220, 115, 140, self.x, self.y)
            #draw_rectangle(self.x - 50, self.y + 10, self.x - 20, self.y + 25)
        a = self.x - 50
        b = self.y + 10


    def get_bb(self):
        global i
        if i == 100:
            return a ,b,a+30,b+15
        else:
            return 0,0,0,0

    def handle_collision(self, other, group):
        print('kazuya punched by pheonix')


class KICK2:
    def __init__(self):
        self.x = 600
        self.y = 200

    def enter(self, event):
        self.kick_1 = 0
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
        if game_state.p_hit == True:
            i -= 1
            self.image.clip_composite_draw(217, 675, 90, 140,0,'', self.x+5, self.y,80,170)
            if i == 0:
                i = 100
                game_state.p_hit = False
        else:
            self.image.clip_composite_draw((self.kick_1)*80, 1180, 78, 90, 0, 'h', self.x-5, self.y-8, 80, 100)
            #draw_rectangle(self.x-45,self.y+10,self.x - 20,self.y + 30)
        a = self.x - 45
        b = self.y + 10

    def get_bb(self):
        global i
        if i == 100:
            return a ,b,a+25,b+20
        else:
            return 0,0,0,0

    def handle_collision(self, other, group):
        print('kazuya kicked by pheonix')

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, PD: PUNCH2, PU: PUNCH2, KD: KICK2, KU: KICK2},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, PD: PUNCH2, PU: PUNCH2, KD: KICK2, KU: KICK2},
    PUNCH2: {RU: PUNCH2, LU: PUNCH2, RD: PUNCH2, LD: PUNCH2, PU: IDLE, PD: IDLE, KU: PUNCH2, KD: PUNCH2},
    KICK2: {RU: KICK2, LU: KICK2, RD: KICK2, LD: KICK2, PD: KICK2, PU: KICK2, KU: IDLE, KD: IDLE}
}


class PaulPheonix:

    def __init__(self):
        self.x, self.y = 600, 200
        self.frame = 0
        self.fra=0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('Paul pheonix.png')

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
        return self.x - 20, self.y - 50, self.x + 33, self.y + 40

    def handle_collision(self, other, group):
        if defence == False:
            rightlifebar.a += 3
        self.bgm = load_music('kazuya_punch_sound.mp3')
        self.bgm.set_volume(15)
        self.bgm.play()