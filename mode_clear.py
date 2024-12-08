from pico2d import get_events, clear_canvas, update_canvas, load_image, load_music, load_wav, delay
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_RETURN, SDLK_ESCAPE

import handle_framework


def init_mode():
    global image
    image = load_image('clear.png')

    sound = load_music('clearbgm.mp3')
    sound.set_volume(100)
    delay(0.5)
    sound.play()
    pass


####################
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            handle_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            handle_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            handle_framework.quit()
    pass


def update():
    pass


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
