from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music
from sdl2 import SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE, SDL_KEYUP, SDLK_KP_ENTER, SDLK_RETURN

import game_world
import handle_framework
import lilly
import mode_play


def init_mode():
    global image, sound
    image = load_image('title.png')


    sound = load_music('titlebgm.mp3')
    sound.set_volume(100)
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
            handle_framework.change_mode(mode_play)
    pass


def update():
    sound.play()
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass


def finish():
    global image, sound
    del sound
    del image


def pause():pass
def resume():pass


