from pico2d import*

from lilly import Lilly


#뭐가 많이 안되니까 일단 미뤄뒀다가 다음에 해보자고..


##
def reset_world():
    global world
    global running
    
    global lilly
    
    running = True
    world = []

    lilly = Lilly()

    world.append(lilly)
    pass


def update_world():
    for objt in world:
        objt.update()
    pass


def render_world():
    clear_canvas()
    for objt in world:
        objt.draw()
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
