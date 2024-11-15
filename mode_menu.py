from pico2d import load_image, get_events, update_canvas, clear_canvas
from sdl2 import SDL_KEYDOWN, SDLK_RETURN, SDLK_ESCAPE, SDL_QUIT, SDLK_1, SDLK_KP_1, SDLK_KP_2

import handle_framework
import mode_title


def init_mode():
    global image
    image = load_image('menu.png')
    pass



####################
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            handle_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            handle_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_KP_1:
            handle_framework.pop_mode()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_KP_2:
            handle_framework.change_mode(mode_title)
    pass



def update():pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass


def finish():
    global image
    del image


def pause():pass
def resume():pass

