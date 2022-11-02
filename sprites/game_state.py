from pico2d import *
import game_framework
from background import BackGround
background = None
from jin import Jin
jin = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()
        else:
            #boy.handle_event(event)
            pass

def enter():
    global background
    background = BackGround()

def exit():
    global background
    del background

def update():
    pass

def draw_world():
    background.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import game_state

    pico2d.open_canvas()
    game_framework.run(game_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()