from pico2d import clear_canvas, update_canvas, get_events
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDLK_ESCAPE, SDL_QUIT

import game_world
import handle_framework
import mode_menu
from lilly import Lilly
from stagetwo_info import Background2, Ground_Two, Bridge


def init_mode():
    global lilly
    global community


    lilly = Lilly()
    game_world.add_object(lilly,3)

#BACKGROUND-----
#    background_two = Background2()
#    game_world.add_object(background_two, 0)
#GROUND-----
    ground2 = Ground_Two(lilly)
    game_world.add_object(ground2,1)
    game_world.add_collision_info('lilly:tempground', None, ground2)

    lilly.get_GF_info(ground2)

#BRIDGE-----
#    bridge = Bridge(1500,180)
#    bridge.get_GF_cam_info(ground2)
#    game_world.add_object(bridge,2)





#SHIFTOBJT-----
#    shift_1to2 = ShiftObjt2(7650,290)
#    shift_1to2.get_GF_cam_info(tempground)
#    game_world.add_object(shift_1to2, 2)
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