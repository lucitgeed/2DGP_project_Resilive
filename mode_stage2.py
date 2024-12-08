from pico2d import clear_canvas, update_canvas, get_events
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDLK_ESCAPE, SDL_QUIT

import game_world
import handle_framework
import mode_menu
from eyes import Eyes
from lilly import Lilly
from stagetwo_info import ObstacleWater, ObstacleThorn, ShiftObjt2
from stagetwo_info import Background2, Ground_Two, Bridge, CarBus, CarGreen, CarRed, CarWhiteStrange, CarWhite


def init_mode():
    global lilly
    global community


    lilly = Lilly()
    game_world.add_object(lilly,6)

#BACKGROUND-----
    background_two = Background2()
    game_world.add_object(background_two, 0)
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
    bus1 = CarBus(1590,140,330,330)
    bus1.get_GF_cam_info(ground2)
    game_world.add_object(bus1,3)
    game_world.add_collision_info('lilly:car', lilly, bus1)

    cargreen1 = CarGreen(4000, 120, 250,250)
    cargreen1.get_GF_cam_info(ground2)
    game_world.add_object(cargreen1, 3)
    game_world.add_collision_info('lilly:car', lilly,cargreen1)

#    carred1 = CarRed(6600, 120, 250,250)
#    carred1.get_GF_cam_info(ground2)
#    game_world.add_object(carred1, 3)
#    game_world.add_collision_info('lilly:car', lilly,carred1)

    carwhite1 = CarWhiteStrange(4400,120,250,250)
    carwhite1.get_GF_cam_info(ground2)
    game_world.add_object(carwhite1, 3)

#    carwhite2 = CarWhite(6000,120,250,250)
#    carwhite2.get_GF_cam_info(ground2)
#    game_world.add_object(carwhite2, 3)
#    game_world.add_collision_info('lilly:car', lilly, carwhite2)

#EYES-----
    eye1 = Eyes(lilly,3500, 500)
    eye1.get_GF_cam_info(ground2)
    game_world.add_object(eye1, 5)
    game_world.add_collision_info('lilly:eye', lilly, eye1)

    eye2 = Eyes(lilly,4500, 500)
    eye3 = Eyes(lilly,5500, 500)
    eye4 = Eyes(lilly, 6000, 500)
    eye5 = Eyes(lilly, 7500, 500)

    eye2.get_GF_cam_info(ground2)
    eye3.get_GF_cam_info(ground2)
    eye4.get_GF_cam_info(ground2)
    eye5.get_GF_cam_info(ground2)

    game_world.add_object(eye2, 5)
    game_world.add_object(eye3, 5)
    game_world.add_object(eye4, 5)
    game_world.add_object(eye5, 5)

    game_world.add_collision_info('lilly:eye', lilly, eye2)
    game_world.add_collision_info('lilly:eye', lilly, eye3)
    game_world.add_collision_info('lilly:eye', lilly, eye4)
    game_world.add_collision_info('lilly:eye', lilly, eye5)

#OBST-----
    water9 = ObstacleWater(lilly,1443,58, 180)
    water9.get_GF_cam_info(ground2)
    game_world.add_object(water9,7)
    game_world.add_collision_info('lilly:water',lilly,water9)

    thorn1 = ObstacleThorn(lilly, 3830, 28, 130)
    thorn1.get_GF_cam_info(ground2)
    game_world.add_object(thorn1,7)
    game_world.add_collision_info('lilly:thorn', lilly, thorn1)
    thorn2 = ObstacleThorn(lilly, 4400, 28, 120)
    thorn2.get_GF_cam_info(ground2)
    game_world.add_object(thorn2, 7)
    game_world.add_collision_info('lilly:thorn', lilly, thorn2)

#SHIFTOBJT-----
#    shift_2to3 = ShiftObjt2(7900,120)
#    shift_2to3.get_GF_cam_info(ground2)
#    game_world.add_object(shift_2to3, 4)
#    game_world.add_collision_info('lilly:shift_2th3', lilly, shift_2to3)
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