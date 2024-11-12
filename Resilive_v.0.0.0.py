from pico2d import*

import game_world
from community import Community
from lilly import Lilly



##
def reset_world():
    global world
    global running
    
    global lilly
    global community
    
    running = True

    lilly = Lilly()
    game_world.add_object(lilly,0)

    community = [Community() for i in range(5)]
    game_world.add_objts(community, 1)
    pass


def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if event.type in (SDL_KEYDOWN, SDL_KEYUP):
                lilly.handle_event(event)




##
open_canvas()

reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
    pass

close_canvas()
