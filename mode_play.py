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

from stageone_info import Ground_One, ObstacleWater, Background1, ShiftObjt1, Pipe, PipeStrong, PipeWeak


#for parallax scrolling
#background_near = None
#background_middle = None

#camera_x = 0
#camera_y = 0

#set scroll speed
#SCROLL_SPEED_NEAR = 100
#SCROLL_SPEED_MIDDLE = 50




def init_mode():
    global lilly
    global community
    global stage_one, tempground


    lilly = Lilly()
    game_world.add_object(lilly,3)

#    background_one = Background1()
#    game_world.add_object(background_one, 0)


    tempground = Ground_One(lilly)
    game_world.add_object(tempground,1)
    game_world.add_collision_info('lilly:tempground', None, tempground)

    lilly.get_GF_info(tempground)


    water = ObstacleWater(lilly,3634,58, 132)
    water.get_GF_cam_info(tempground)

    game_world.add_object(water,4)
#    game_world.add_collision_info('lilly:water', lilly, water)
    #
    water2 = ObstacleWater(lilly, 5050-433, 58, 433)
    water3 = ObstacleWater(lilly, 5050, 58, 433)
    water4 = ObstacleWater(lilly, 5050 +433,58, 433)
    watertemp = []
    watertemp.append(water2)
    watertemp.append(water3)
    watertemp.append(water4)
    water2.get_GF_cam_info(tempground)
    water3.get_GF_cam_info(tempground)
    water4.get_GF_cam_info(tempground)

    game_world.add_objts(watertemp, 4)
#    game_world.add_collision_info('lilly:water', lilly,water2)
#    game_world.add_collision_info('lilly:water', lilly,water3)
#    game_world.add_collision_info('lilly:water', lilly,water4)

    pipe1 = PipeStrong(3710,150, 256,256)
    pipe1.get_GF_cam_info(tempground)
    game_world.add_object(pipe1,5)
    game_world.add_collision_info('lilly:pipe', lilly, pipe1)

    pipe2 = PipeWeak(5000, 108, 512, 512)
    pipe2.get_GF_cam_info(tempground)
    game_world.add_object(pipe2, 5)
    game_world.add_collision_info('lilly:pipe', lilly, pipe2)


#    shift_1to2 = ShiftObjt1()
#    game_world.add_object(shift_1to2, 2)
#    game_world.add_collision_info("lilly:shift_1to2", lilly, None)


    game_world.add_collision_info('lilly:cmity_aggro', lilly, None)
#    game_world.add_collision_info('lilly:cmity_attck', lilly, None)



#    eyeLIDS = [Eyelid() for _ in range(5)]
#    game_world.add_objts(eyeLIDS, 3)



    community = [Community() for _ in range(3)]
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

                for c in community:
                    c.handle_event()


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