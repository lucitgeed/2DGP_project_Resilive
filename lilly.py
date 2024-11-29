from ast import Param

from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, delay, \
    draw_rectangle, clamp

import game_world
import handle_framework
from StateMachine import*
from game_world import remove_collision_objt

PIXEL_per_METER = (10.0 / 1)      # 1pixel = 10cm
# set lilly speed
#RUN_SPEED_KM_per_H = 17.0
RUN_SPEED_KM_per_H = 50.0

RUN_SPEED_M_per_M = (RUN_SPEED_KM_per_H * 1000.0 / 60.0)
RUN_SPEED_M_per_S = RUN_SPEED_M_per_M / 60.0
RUN_SPEED_PPS = RUN_SPEED_M_per_S * PIXEL_per_METER

WALK_SPEED_KM_per_H = 6.5
WALK_SPEED_M_per_M = (WALK_SPEED_KM_per_H * 1000.0 / 60.0)
WALK_SPEED_M_per_S = WALK_SPEED_M_per_M / 60.0
WALK_SPEED_PPS = WALK_SPEED_M_per_S * PIXEL_per_METER

JUMP_SPEED_MPS = 15
JUMP_SPEED_PPS  = JUMP_SPEED_MPS * PIXEL_per_METER

CRAWL_SPEED_KM_per_H= 6
CRAWL_SPEED_M_per_M = (CRAWL_SPEED_KM_per_H * 1000.0 / 60.0)
CRAWL_SPEED_M_per_s = CRAWL_SPEED_M_per_M / 60.0
CRAWL_SPEED_PPS = CRAWL_SPEED_M_per_s * PIXEL_per_METER

# set frame flip speed
TIME_per_Idle_ACTION = 0.8
Idle_ACTION_per_TIME = 1.0 / TIME_per_Idle_ACTION

TIME_per_Walk_ACTION = 0.8
Walk_ACTION_per_TIME = 1.0 / TIME_per_Walk_ACTION

TIME_per_Run_ACTION = 0.6
Run_ACTION_per_TIME = 1.0 / TIME_per_Run_ACTION

TIME_per_Jump_ACTION = 2
Jump_ACTION_per_TIME = 1.0 / TIME_per_Jump_ACTION

TIME_per_Crawl_ACTION = 1.5
Crawl_ACTION_per_TIME = 1.0 / TIME_per_Crawl_ACTION





class Lilly:
    image = None

    def __init__(self):
        self.x, self.y = 50,120
        self.face_dir = 1

        if Lilly.image == None:
            Lilly.imageIdle = load_image("lilly_idle_Sheet.png")
            Lilly.imageRun = load_image("lilly_run_Sheet.png")
            Lilly.imageJump = load_image("lilly_jump-Sheet.png")
            Lilly.imageWalk = load_image("lilly_walk_Sheet.png")
            Lilly.imageCrawl = load_image("lilly_crawl-Sheet.png")

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle:{right_down:Walk, right_up:Idle, left_down:Walk, left_up:Idle, shift_down:Idle,
                      space_down:Jump,
                      caughtby_cmity:Caught,
                      ctrl_down:Crawl},

                Walk:{right_down:Idle, right_up:Idle, left_down:Idle, left_up:Idle,
                      shift_down:Run,
                      space_down:Jump,
                      caughtby_cmity:Caught,
                      ctrl_down:Crawl},

                Run:{shift_up:Walk, right_up:Idle, left_up:Idle,
                     right_down:Run, left_down:Run,
                     space_down:Jump,
                     caughtby_cmity:Caught,
                     ctrl_down:Crawl},

                Jump:{right_down:Jump_andMOVE, left_down:Jump_andMOVE},
                Jump_andMOVE:{landed:Idle, right_down:Jump_andMOVE, left_down:Jump_andMOVE},

                Crawl:{ctrl_down:Crawl, right_down:Crawl, left_down:Crawl, right_up:Crawl, left_up:Crawl,
                       space_down:Jump, ctrl_up:Idle}

#                Caught:{time_out:Dead,in_time:Idle}
            }
        )


    def update(self):
        self.state_machine.update()

        self.x = clamp(25,
                       self.x,
                       self.groundfloor_w - 20)
        self.y = clamp(10,
                       self.y,
                       self.groundfloor_h - 10)


    def handle_event(self, event):
        self.state_machine.add_events(
            ('Input', event)
        )

    def draw(self):
        self.state_machine.draw()

        draw_rectangle(*self.get_boundingbox())             # * 붙이는거 잊지말것!!!!
        draw_rectangle(*self.get_aggrobox())

    #-----------------
    def get_boundingbox(self):
        return (self.x-25, self.y-40, self.x+17, self.y+35)

    def get_aggrobox(self):
        return (self.x-45, self.y-60,self.x+37, self.y+55)

    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:community':
            pass
        if crashgroup == 'lilly:cmity_aggro':
            pass
        if crashgroup == 'lilly:cmity_attack':
            pass

        if crashgroup == 'lilly:tempground':
            self.state_machine.add_events(('Landed',0))
            game_world.remove_a_collision_objt('lilly:tempground', self)
#            game_world.remove_collision_objt(self)
#           self.state_machine.cur_state.handle_self_collision(crashgroup, other)

        if crashgroup == 'lilly:water':
            game_world.remove_collision_objt(self)
            game_world.remove_objt(self)
            pass

#-----------------------------------------------------
    def get_BG_info(self, background_w, background_h):
        self.background_w = background_w
        self.background_h = background_h

    def get_GF_info(self, groundfloor_w, groundfloor_h):
        self.groundfloor_w = groundfloor_w
        self.groundfloor_h = groundfloor_h





#############
class Idle:
    @staticmethod
    def enter(lilly, e):

        if start_event(e):
            lilly.face_dir = 1
        elif right_up(e):
            lilly.face_dir = 1
            lilly.dir = 0
        elif left_up(e):
            lilly.face_dir = -1
            lilly.dir = 0

        if landed(e):
            lilly.y += JUMP_SPEED_PPS * handle_framework.frame_time + 2
            pass

        lilly.frame = 0
        lilly.dir = 0

    @staticmethod
    def exit(lilly, e):

        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame + 5 * Idle_ACTION_per_TIME * handle_framework.frame_time) % 5
        pass

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == 1:
            lilly.imageIdle.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 80,80)
        elif lilly.face_dir == -1:
            lilly.imageIdle.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128,
                                                0,'h', lilly.x, lilly.y, 80,80)

    #-------
    @staticmethod
    def handle_self_collision(lilly):
        pass




class Walk:
    @staticmethod
    def enter(lilly, e):
        if right_down(e):
            lilly.face_dir = 1
            lilly.dir = 1
        elif right_up(e):
            lilly.dir = 0

        elif left_down(e):
            lilly.face_dir = -1
            lilly.dir = -1
        elif left_up(e):
            lilly.dir = 0

        if landed(e):
            lilly.y += JUMP_SPEED_PPS * handle_framework.frame_time + 2

    @staticmethod
    def exit(lilly,e):
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame+ 10 * Walk_ACTION_per_TIME * handle_framework.frame_time) % 10

        lilly.x += lilly.dir * WALK_SPEED_PPS * handle_framework.frame_time
#        delay(0.04)

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageWalk.clip_draw(int(lilly.frame)*128,0, 128,128, lilly.x, lilly.y, 80,80)
        elif lilly.face_dir == 1:
            lilly.imageWalk.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0,'h', lilly.x, lilly.y, 80,80)




class Run:
    @staticmethod
    def enter(lilly, e):
        if right_down(e):
            lilly.face_dir = 1
            lilly.dir = 1
        elif right_up(e):
            lilly.dir = 0
        elif left_down(e):
            lilly.face_dir = -1
            lilly.dir = -1
        elif left_up(e):
            lilly.dir = 0


        if landed(e):
            lilly.y += JUMP_SPEED_PPS * handle_framework.frame_time + 2

    @staticmethod
    def exit(lilly, e):
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame+ 8* Run_ACTION_per_TIME * handle_framework.frame_time) % 8

        lilly.x += lilly.dir * RUN_SPEED_PPS * handle_framework.frame_time

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageRun.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 80,80)
        elif lilly.face_dir == 1:
            lilly.imageRun.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 80,80)




class Jump:
    @staticmethod
    def enter(lilly, e):
        lilly.frame = 0
        lilly.head_dir = 1
        lilly.jump_vel_dir = 1

        game_world.add_collision_info('lilly:tempground', lilly, None)

    @staticmethod
    def exit(lilly, e):
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame + 18* Jump_ACTION_per_TIME*handle_framework.frame_time) % 18

        if 25 <= lilly.x <= 800 - 25:
            pass
        elif lilly.x < 25:
            lilly.x = 25
        elif lilly.x > 800 - 25:
            lilly.x = 800 - 25

        if 50 <= lilly.y <= 550:
            lilly.y +=lilly.jump_vel_dir * JUMP_SPEED_PPS *  handle_framework.frame_time

            if int(lilly.y) == 250:
                lilly.jump_vel_dir = -1
        elif lilly.y < 50:
            lilly.y =50
        elif lilly.y > 550:
            lilly.y = 550



    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageJump.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 80,80)
        elif lilly.face_dir == 1:
            lilly.imageJump.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 80,80)

    #--------
#    @staticmethod
#    def handle_self_collision(lilly):
#        lilly.state_machine.add_events(('Landed', 0))


class Jump_andMOVE:
    @staticmethod
    def enter(lilly, e):
        lilly.frame = 0
        lilly.jump_vel_dir = 1

        game_world.add_collision_info('lilly:tempground', lilly, None)

        if right_down(e) or left_up(e):
            lilly.dir = 1
        elif left_down(e) or right_up(e):
            lilly.dir = -1

    @staticmethod
    def exit(lilly, e):
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame + 18* Jump_ACTION_per_TIME*handle_framework.frame_time) % 18

        if 25 <= lilly.x <= 800 - 25:
            lilly.x += lilly.dir * JUMP_SPEED_PPS * handle_framework.frame_time /3*2
        elif lilly.x < 25:
            lilly.x = 25
        elif lilly.x > 800 - 25:
            lilly.x = 800 - 25

        if 50 <= lilly.y <= 550:
            lilly.y += lilly.jump_vel_dir * JUMP_SPEED_PPS * handle_framework.frame_time

            if int(lilly.y) == 250:
                lilly.jump_vel_dir = -1
        elif lilly.y < 50:
            lilly.y = 50
        elif lilly.y > 550:
            lilly.y = 550

    @staticmethod
    def draw(lilly):
        if lilly.dir == -1:
            lilly.imageJump.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 80,80)
        elif lilly.dir == 1:
            lilly.imageJump.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 80,80)




class Crawl:
    @staticmethod
    def enter(lilly, e):
        lilly.frame = 0
        if ctrl_down(e):
            lilly.boxdevide = 2

        if right_down(e):
            lilly.face_dir = 1
            lilly.dir = 1
        elif left_up(e):
            lilly.face_dir = -1
            lilly.dir = 0
        elif left_down(e):
            lilly.face_dir = -1
            lilly.dir = -1
        elif right_up(e):
            lilly.face_dir = 1
            lilly.dir = 0
        pass

    @staticmethod
    def exit(lilly, e):
        if ctrl_up(e):
            pass
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame + 7* Crawl_ACTION_per_TIME * handle_framework.frame_time) % 7

        lilly.x += lilly.dir * CRAWL_SPEED_PPS * handle_framework.frame_time

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageCrawl.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 80,80)
        elif lilly.face_dir == 1:
            lilly.imageCrawl.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 80,80)



class Caught:
    @staticmethod
    def enter():
        pass
    @staticmethod
    def exit():
        pass
    @staticmethod
    def do():
        pass
    @staticmethod
    def draw():
        pass

