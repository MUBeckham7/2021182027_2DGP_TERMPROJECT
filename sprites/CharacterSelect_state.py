from pico2d import *
import game_framework
import game_state
from character_select import Character_select
character_select = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            game_framework.change_state(game_state)

def enter():
    global character_select
    character_select = Character_select()

def exit():
    global character_select
    del character_select

def update():
    pass

def draw_world():
    character_select.draw()

def draw():
    clear_canvas()
    draw_world()
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