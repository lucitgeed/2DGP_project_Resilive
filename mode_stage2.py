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

from stageone_info import Ground_One, ObstacleWater, Background1, ShiftObjt1, PipeStrong, PipeWeak, PipeFragile, \
    RealShift1




def init_mode():
    global lilly
    global community


    lilly = Lilly()
    game_world.add_object(lilly,3)

#BACKGROUND-----
#    background_one = Background1()
#    game_world.add_object(background_one, 0)
#GROUND-----
    tempground = Ground_One(lilly)
    game_world.add_object(tempground,1)
    game_world.add_collision_info('lilly:tempground', None, tempground)

    lilly.get_GF_info(tempground)


#SHIFTOBJT-----
    shift_1to2 = ShiftObjt1(7650,290)
    shift_1to2.get_GF_cam_info(tempground)
    game_world.add_object(shift_1to2, 2)
    game_world.add_collision_info("lilly:shift_1to2", lilly, shift_1to2)


#    eyeLIDS = [Eyelid() for _ in range(5)]
#    game_world.add_objts(eyeLIDS, 3)



#    community = [Community() for _ in range(3)]
#    game_world.add_objts(community, 3)
#    for c in community:
#        game_world.add_collision_info('lilly:cmity_aggro', None, c)


#        game_world.add_collision_info('lilly:cmity_attck', None, c)



#    eyePUPILS = [Eyepupil() for i in range(10)]
#    game_world.add_objts(eyePUPILS, 4)


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


def update():
    game_world.update()
    game_world.handle_collisions()
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