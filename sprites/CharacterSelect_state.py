from pico2d import *
import game_framework
import game_state
import game_world
from character_select import Character_select
from jin_portrait import JIN_Portrait
from kazuya_portrait import Kazuya_Portrait
from haeiachi_portrait import Haeiachi_Portrait
character_select = None
jin_portrait = None
kazuya_portrait = None
haeiachi_portrait = None
x1,x2=0,0
change_count=0

def handle_events():
    global x1,x2,change_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_d):
            x1 += 100
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            x1 -= 100
        elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
            x2 += 100
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            x2 -= 100
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            game_framework.change_state(game_state)


def enter():
    global character_select,jin_portrait,kazuya_portrait,haeiachi_portrait
    character_select = Character_select()
    jin_portrait = JIN_Portrait()
    kazuya_portrait = Kazuya_Portrait()
    haeiachi_portrait = Haeiachi_Portrait()
    game_world.add_object(character_select, 0)
    game_world.add_object(jin_portrait,1)
    game_world.add_object(kazuya_portrait,1)
    game_world.add_object(haeiachi_portrait,1)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    global x1,x2
    clear_canvas()
    draw_world()
    draw_rectangle(102+x1,85,195+x1,176)
    draw_rectangle(600+x2,85,700+x2,176)
    update_canvas()

def pause():
    pass

def resume():
    pass
def test_self():
    import title_state

    pico2d.open_canvas()
    game_framework.run(title_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()