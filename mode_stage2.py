from pico2d import clear_canvas, update_canvas, get_events
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDLK_ESCAPE, SDL_QUIT

import game_world
import handle_framework
import mode_menu
from eyes import Eyes
from lilly import Lilly
from stagetwo_info import ObstacleWater
from stagetwo_info import Background2, Ground_Two, Bridge, CarBus, CarGreen, CarRed, CarWhiteStrange, CarWhite


def init_mode():
    global lilly
    global community


    lilly = Lilly()
    game_world.add_object(lilly,6)

#BACKGROUND-----
#    background_two = Background2()
#    game_world.add_object(background_two, 0)
#GROUND-----
    ground2 = Ground_Two(lilly)
    game_world.add_object(ground2,2)
    game_world.add_collision_info('lilly:tempground', None, ground2)

    lilly.get_GF_info(ground2)

#BRIDGE-----
#    bridge = Bridge(1500,180)
#    bridge.get_GF_cam_info(ground2)
#    game_world.add_object(bridge,1)


#CARS-----
    bus1 = CarBus(1700,140,330,330)
    bus1.get_GF_cam_info(ground2)
    game_world.add_object(bus1,3)
    game_world.add_collision_info('lilly:car', lilly, bus1)

    cargreen1 = CarGreen(2700, 120, 250,250)
    cargreen1.get_GF_cam_info(ground2)
    game_world.add_object(cargreen1, 3)
    game_world.add_collision_info('lilly:car', lilly,cargreen1)

    carred1 = CarRed(2700, 120, 250,250)
    carred1.get_GF_cam_info(ground2)
    game_world.add_object(carred1, 3)
    game_world.add_collision_info('lilly:car', lilly,carred1)

    carwhite1 = CarWhiteStrange(6600,120,250,250)
    carwhite1.get_GF_cam_info(ground2)
    game_world.add_object(carwhite1, 3)
    game_world.add_collision_info('lilly:car', lilly,carwhite1)

    carwhite2 = CarWhite(6000,120,250,250)
    carwhite2.get_GF_cam_info(ground2)
    game_world.add_object(carwhite2, 3)
    game_world.add_collision_info('lilly:car', lilly, carwhite2)

#EYES-----
#    eye1 = Eyes(lilly,3500, 500)
#    eye1.get_GF_cam_info(ground2)
#    game_world.add_object(eye1, 5)
#    game_world.add_collision_info('lilly:eye', lilly, eye1)


#    eye2 = Eyes(lilly,3500, 500)
#    eye3 = Eyes(lilly,3500, 500)




#    eye2.get_GF_cam_info(ground2)
#    game_world.add_object(eye2, 5)
#    game_world.add_collision_info('lilly:eye', lilly, eye2)


#    eye1.get_GF_cam_info(ground2)
#    game_world.add_object(eye1, 5)
#    game_world.add_collision_info('lilly:eye', lilly, eye1)

#    eye1 = Eyes(lilly,3500, 500)
#    eye1.get_GF_cam_info(ground2)
#    game_world.add_object(eye1, 5)
#    game_world.add_collision_info('lilly:eye', lilly, eye1)

#    eye1 = Eyes(lilly,3500, 500)
#    eye1.get_GF_cam_info(ground2)
#    game_world.add_object(eye1, 5)
#    game_world.add_collision_info('lilly:eye', lilly, eye1)

#OBST-----
    water9 = ObstacleWater(lilly,6900,58, 132)
    water9.get_GF_cam_info(ground2)
    game_world.add_object(water9,7)
    game_world.add_collision_info('lilly:water',lilly,water9)

#SHIFTOBJT-----
#    shift_1to2 = ShiftObjt2(7650,290)
#    shift_1to2.get_GF_cam_info(tempground)

#    game_world.add_object(shift_1to2, 4)

#    game_world.add_collision_info("lilly:shift_1to2", lilly, shift_1to2)


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