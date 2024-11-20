from pico2d import get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_KEYUP

import game_world
import handle_framework
import lilly
import mode_menu
from community import Community
from eyelid import Eyelid
from eyepupil import Eyepupil
from game_world import add_object
from lilly import Lilly
from stage_ground import Ground_One, StageOne


def init_mode():
    global lilly
    global community

#    stage_one = StageOne()
#    game_world.add_object(stage_one,0)

    lilly = Lilly()
    game_world.add_object(lilly,1)

    game_world.add_collision_info('lilly:cmity_aggro', lilly, None)
#    game_world.add_collision_info('lilly:cmity_attck', lilly, None)


#    eyeLIDS = [Eyelid() for i in range(5)]
#    game_world.add_objts(eyeLIDS, 1)

    community = [Community() for _ in range(5)]
    game_world.add_objts(community, 2)
    for c in community:
        game_world.add_collision_info('lilly:cmity_aggro', None, c)
#        game_world.add_collision_info('lilly:cmity_attck', None, c)

#    eyePUPILS = [Eyepupil() for i in range(10)]
#    game_world.add_objts(eyePUPILS, 1)

    tempground = Ground_One()
    game_world,add_object(tempground,0)

    game_world.add_collision_info('lilly:tempground', None, tempground)


    #collision info
#    game_world.add_collision_info('lilly:community',lilly, None)
#    game_world.add_collision_info('lilly:cmity_aggro', lilly, None)
#    for cmity in community:
#        game_world.add_collision_info('lilly:community', None, cmity)
#        game_world.add_collision_info('lilly:cmity_aggro', None, cmity)


    pass



########################
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            handle_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            handle_framework.push_mode(mode_menu)
            pass
        else:
            if event.type in (SDL_KEYDOWN, SDL_KEYUP):
                lilly.handle_event(event)

                for c in community:
                    c.handle_event()


def update():
    game_world.update()

    game_world.handle_collisions()
    game_world.handle_death_collisions()

    pass


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
    pass


def finish():
    game_world.clear()


def pause():pass
def resume():pass