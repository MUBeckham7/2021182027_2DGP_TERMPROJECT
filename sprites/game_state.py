from pico2d import *
import game_framework
import game_world
import pygame
import game_framework
import title_state
import CharacterSelect_state

from background import BackGround
from jin import Jin
from kazuya import Kazuya
from paulpheonix import PaulPheonix
from gameover import GameOver
from lifebar import LifeBar
from leftlifebar import LeftLifeBar
from rightlifebar import RightLifeBar
from timefont import Timefont
from jin import PUNCH
from kazuya import PUNCH1
from paulpheonix import PUNCH2
from jin import KICK
from kazuya import KICK1
from paulpheonix import KICK2
from win import Win

background = None
jin = None
kazuya = None
paulpheonix = None
gameover=None
gameoverTF = False
start_ticks =None
lifebar = None
leftlifebar=None
rightlifebar = None
sec=0
i=700
k=700
total_time = 100
timefont = None
elapsed_time = 0
jinPunch = None
kazuya_Punch = None
paulPunch = None
jinKick = None
kazuyaKick = None
paulKick = None
k_hit = False
j_hit = False
p_hit = False
win = None
jin_win_count = 0
kazuya_win_count = 0


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            if CharacterSelect_state.x1 == 0:
                jin.handle_event(event)
                print(CharacterSelect_state.x1,'jin')
            if CharacterSelect_state.x2 == 0:
                kazuya.handle_event(event)
                print(CharacterSelect_state.x2,'kazuya')
            if CharacterSelect_state.x2 == -100:
                paulpheonix.handle_event(event)
                print(CharacterSelect_state.x2,'pheonix')


def enter():
    global background,lifebar,leftlifebar,rightlifebar
    global start_ticks,gameover,gameoverTF,timefont
    global win
    if CharacterSelect_state.x1 == 0:           #######진
        global jin,jinPunch,jinKick
        jin=Jin()
        jinPunch = PUNCH()
        jinKick = KICK()
        game_world.add_object(jin, 1)

    if CharacterSelect_state.x2 == 0:           #######카주야
        global kazuya, kazuyaKick,kazuya_Punch
        kazuya=Kazuya()
        kazuya_Punch = PUNCH1()
        kazuyaKick = KICK1()
        game_world.add_object(kazuya, 1)
    if CharacterSelect_state.x2 == -100:        ########폴 피닉스
        global paulpheonix,paulPunch,paulKick
        paulpheonix = PaulPheonix()
        paulPunch = PUNCH2()
        paulKick = KICK2()
        game_world.add_object(paulpheonix,1)


    background = BackGround()
    gameover = GameOver()
    lifebar = LifeBar()
    leftlifebar = LeftLifeBar()
    rightlifebar= RightLifeBar()
    timefont = Timefont()


    win = Win()
    game_world.add_object(background, 0)


    game_world.add_object(lifebar,1)
    game_world.add_object(leftlifebar,1)
    game_world.add_object(rightlifebar,1)
    game_world.add_object(timefont,1)
    game_world.add_object(win,1)
    #game_world.add_collision_group(jin,kazuya,'jin:kazuya')

    # x1 == 0 진 , x2 == 0 카주야 , x2 == -100

    if CharacterSelect_state.x1 == 0 and CharacterSelect_state.x2 == 0:
        game_world.add_collision_group(jinPunch,kazuya,'jinpunch:kazuya')
        game_world.add_collision_group(jinKick,kazuya,'jinKick:kazuya')
        game_world.add_collision_group(kazuya_Punch, jin, 'kazuya_Punch:jin')
        game_world.add_collision_group(kazuyaKick, jin, 'kazuyaKick:jin')

    if CharacterSelect_state.x1 == 0 and CharacterSelect_state.x2 == -100:
        game_world.add_collision_group(jinKick, paulpheonix, 'jinKick:paulpheonix')
        game_world.add_collision_group(jinPunch, paulpheonix, 'jinpunch:paulpheonix')
        game_world.add_collision_group(paulPunch,jin,'paulpunch:jin')
        game_world.add_collision_group(paulKick,jin,'paulkick:jin')







    start_ticks = pygame.time.get_ticks()
def exit():
    game_world.clear()
    global k_hit,j_hit,p_hit
    k_hit ,j_hit ,p_hit= False,False,False
    CharacterSelect_state.x1 ,CharacterSelect_state.x2 = 0, 0

def update():
    global sec,gameoverTF,elapsed_time,total_time,k_hit,j_hit,p_hit

    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('Collision by', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
            if b == kazuya:
                k_hit = True
            if b == jin:
                j_hit = True
            if b== paulpheonix:
                p_hit = True

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            # display_time(total_time - int(elapsed_time))

    if total_time - int(elapsed_time) <= 0:
        game_world.add_object(gameover, 1)

    import rightlifebar
    import leftlifebar
    if leftlifebar.a >= 164:
        global i,kazuya_win_count
        game_world.add_object(gameover, 1)
        i -= 1
        if i == 0:
            i=700
            game_world.remove_object(gameover)
            leftlifebar.a = 0
            rightlifebar.a = 0
            kazuya_win_count +=1
            game_framework.change_state(title_state)

    if rightlifebar.a >= 164:
        global k,jin_win_count
        game_world.add_object(gameover , 1)
        k -= 1
        if k == 0:
            k=700
            game_world.remove_object(gameover)
            rightlifebar.a = 0
            leftlifebar.a = 0
            jin_win_count += 1
            game_framework.change_state(title_state)


    if total_time - int(elapsed_time) <= -3:
        sec += 1
        game_framework.change_state(title_state)


    if sec == 50:
        sec =  0


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()


    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True


def test_self():
    import game_state

    pico2d.open_canvas()
    game_framework.run(game_state)
    pico2d.clear_canvas()


if __name__ == '__main__':
    test_self()