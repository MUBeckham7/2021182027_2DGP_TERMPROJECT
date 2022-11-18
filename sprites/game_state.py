from pico2d import *
import game_framework
import game_world
import pygame
import game_framework
import title_state

from background import BackGround
from jin import Jin
from kazuya import Kazuya
from gameover import GameOver
from lifebar import LifeBar
from leftlifebar import LeftLifeBar
from rightlifebar import RightLifeBar
from timefont import Timefont
from jin import PUNCH
from kazuya import PUNCH1
from jin import KICK
from kazuya import KICK1

background = None
jin = None
kazuya = None
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
jinKick = None
kazuyaKick = None



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            jin.handle_event(event)
            kazuya.handle_event(event)


def enter():
    global background,jin,kazuya,lifebar,leftlifebar,rightlifebar
    global start_ticks,gameover,gameoverTF,timefont,jinPunch,kazuya_Punch
    global jinKick,kazuyaKick
    jin=Jin()
    kazuya=Kazuya()
    background = BackGround()
    gameover = GameOver()
    lifebar = LifeBar()
    leftlifebar = LeftLifeBar()
    rightlifebar= RightLifeBar()
    timefont = Timefont()
    jinPunch = PUNCH()
    kazuya_Punch = PUNCH1()
    jinKick = KICK()
    kazuyaKick = KICK1()
    game_world.add_object(background, 0)
    game_world.add_object(jin,1)
    game_world.add_object(kazuya,1)
    game_world.add_object(lifebar,1)
    game_world.add_object(leftlifebar,1)
    game_world.add_object(rightlifebar,1)
    game_world.add_object(timefont,1)
    #game_world.add_collision_group(jin,kazuya,'jin:kazuya')
    game_world.add_collision_group(jinPunch,kazuya,'jinpunch:kazuya')
    game_world.add_collision_group(kazuya_Punch,jin,'kazuya_Punch:jin')
    game_world.add_collision_group(jinKick,kazuya,'jinKick:kazuya')
    game_world.add_collision_group(kazuyaKick,jin,'kazuyaKick:jin')


    start_ticks = pygame.time.get_ticks()
def exit():
    game_world.clear()

def update():
    global sec,gameoverTF,elapsed_time,total_time

    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('Collision by', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            # display_time(total_time - int(elapsed_time))

    if total_time - int(elapsed_time) <= 0:
        game_world.add_object(gameover, 1)

    import leftlifebar
    if leftlifebar.a >= 164:
        global i
        game_world.add_object(gameover, 1)
        i -= 1
        if i == 0:
            i=700
            game_world.remove_object(gameover)
            game_framework.change_state(title_state)
            leftlifebar.a = 0

    import rightlifebar
    if rightlifebar.a >= 164:
        global k
        game_world.add_object(gameover , 1)
        k -= 1
        if k == 0:
            k=700
            game_world.remove_object(gameover)
            game_framework.change_state(title_state)
            rightlifebar.a = 0

    if total_time - int(elapsed_time) <= -3:
        game_framework.change_state(title_state)
        sec += 1

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