from ast import Param

from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, delay, \
    draw_rectangle, clamp

import game_world
import handle_framework
import mode_gameover
from StateMachine import*

PIXEL_per_METER = (10.0 / 1)
LILLY_SIZE = 80
# set lilly speed
#RUN_SPEED_KM_per_H = 34.0
RUN_SPEED_KM_per_H = 700.0
RUN_SPEED_M_per_M = (RUN_SPEED_KM_per_H * 1000.0 / 60.0)
RUN_SPEED_M_per_S = RUN_SPEED_M_per_M / 60.0
RUN_SPEED_PPS = RUN_SPEED_M_per_S * PIXEL_per_METER

#WALK_SPEED_KM_per_H = 13
WALK_SPEED_KM_per_H = 100
WALK_SPEED_M_per_M = (WALK_SPEED_KM_per_H * 1000.0 / 60.0)
WALK_SPEED_M_per_S = WALK_SPEED_M_per_M / 60.0
WALK_SPEED_PPS = WALK_SPEED_M_per_S * PIXEL_per_METER

GRAVITY = -10
JUMP_TIME = 4.5
JUMP_SPEED_MPS = 6
JUMP_SPEED_PPS  = JUMP_SPEED_MPS * PIXEL_per_METER

CRAWL_SPEED_KM_per_H= 12
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

TIME_per_Jump_ACTION = 2.5
Jump_ACTION_per_TIME = 1.0 / TIME_per_Jump_ACTION

TIME_per_Crawl_ACTION = 1.5
Crawl_ACTION_per_TIME = 1.0 / TIME_per_Crawl_ACTION





class Lilly:
    image = None
    def __init__(self):
        self.x, self.y = 50,110
        self.x = 6000

        self.cx = 0
        self.face_dir = 1

        self.jump_vel = 0
        self.in_sky = 1

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

                Jump:{right_down:Jump, left_down:Jump, landed:Idle},

                Crawl:{ctrl_down:Crawl, right_down:Crawl, left_down:Crawl, right_up:Crawl, left_up:Crawl,
                       space_down:Jump, ctrl_up:Idle}

#                Caught:{time_out:Dead,in_time:Idle}
            }
        )

        self.hidden = 0


    def update(self):
        self.state_machine.update()

        self.x = clamp(17,
                       self.x,
                       self.ground.width - 17)
        self.y = clamp(35,
                       self.y,
                       self.ground.height - 35)

        self.cx = self.x - self.ground.camera_left
        self.cy = self.y - self.ground.camera_bottom
#        print(f'            lilly.x = {self.x}')
#        print(f'            lilly.cx = {self.cx}')


    def handle_event(self, event):
        self.state_machine.add_events(('Input', event))

    def draw(self):
        self.state_machine.draw()

        draw_rectangle(*self.get_boundingbox())             # * 붙이는거 잊지말것!!!!

    # -----------------

    def get_boundingbox(self):
        return (self.cx-17, self.cy-40, self.cx+17, self.cy+35)
    # -----------------
    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:community':
            pass
        if crashgroup == 'lilly:cmity_aggro':
            pass
        if crashgroup == 'lilly:cmity_attack':
            pass


        if crashgroup == 'lilly:tempground':
            self.state_machine.add_events(('Landed',0))
        if crashgroup == 'lilly:water':
            game_world.remove_objt(self)
            pass
        if crashgroup == 'lilly:pipe':
            self.state_machine.add_events(('Landed',0))
            self.y += JUMP_TIME * handle_framework.frame_time
#            game_world.remove_a_collision_objt('lilly:pipe', self)
            self.in_sky = 0
        if crashgroup == 'lilly:pipe_abouttoCOLLAPSE':
            self.state_machine.add_events(('Landed', 0))
            self.y += JUMP_TIME * handle_framework.frame_time + 2
            self.in_sky = 0
        if crashgroup == 'lilly:shift_1to2':
            game_world.remove_objt(self)


        if crashgroup == 'lilly:car':
            self.state_machine.add_events(('Landed', 0))
            self.y += JUMP_TIME * handle_framework.frame_time
            self.in_sky = 0
            pass
        if crashgroup == 'lilly:thorn':
            game_world.remove_objt(self)
        if crashgroup == 'lilly:eye':
#            game_world.remove_objt(self)
            pass


#-----------------------------------------------------
    def get_GF_info(self, groundfoolr):
        self.ground = groundfoolr





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
            lilly.jump_vel = 0
            lilly.y += JUMP_SPEED_PPS * handle_framework.frame_time + 3

        lilly.frame = 0
        lilly.dir = 0
        lilly.in_sky = 1

    @staticmethod
    def exit(lilly, e):
        if space_down(e):
            lilly.jumping = 1
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame + 5 * Idle_ACTION_per_TIME * handle_framework.frame_time) % 5

        if 115 < lilly.y and lilly.in_sky == 1:
            lilly.y += GRAVITY * handle_framework.frame_time * JUMP_SPEED_PPS
#        lilly.y += JUMP_SPEED_PPS * handle_framework.frame_time + 10

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == 1:
            lilly.imageIdle.clip_draw(int(lilly.frame) * 128, 0, 128, 128,
                                      lilly.cx, lilly.cy,
                                      LILLY_SIZE,LILLY_SIZE)
        elif lilly.face_dir == -1:
            lilly.imageIdle.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128,
                                                0,'h',
                                                lilly.cx, lilly.cy,
                                                LILLY_SIZE,LILLY_SIZE)

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

        lilly.in_sky = 1

    @staticmethod
    def exit(lilly,e):
        if space_down(e):
            lilly.jumping = 1
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame+ 10 * Walk_ACTION_per_TIME * handle_framework.frame_time) % 10
        lilly.x += lilly.dir * WALK_SPEED_PPS * handle_framework.frame_time

        if 115 < lilly.y and lilly.in_sky == 1:
            lilly.y += GRAVITY * handle_framework.frame_time * JUMP_SPEED_PPS

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageWalk.clip_draw(int(lilly.frame)*128,0, 128,128, lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)
        elif lilly.face_dir == 1:
            lilly.imageWalk.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0,'h',
                                                lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)




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

        lilly.in_sky = 1

    @staticmethod
    def exit(lilly, e):
        if space_down(e):
            lilly.jumping = 1
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame+ 8* Run_ACTION_per_TIME * handle_framework.frame_time) % 8

        lilly.x += lilly.dir * RUN_SPEED_PPS * handle_framework.frame_time

        if 115 < lilly.y and lilly.in_sky == 1:
            lilly.y += GRAVITY * handle_framework.frame_time * JUMP_SPEED_PPS



    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageRun.clip_draw(int(lilly.frame) * 128, 0, 128, 128,lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)
        elif lilly.face_dir == 1:
            lilly.imageRun.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h',  lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)




class Jump:
    @staticmethod
    def enter(lilly, e):
        if lilly.jumping == 1:
            lilly.frame = 0

            lilly.jump_vel = JUMP_SPEED_PPS

            game_world.add_collision_info('lilly:tempground', lilly, None)
        else:
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
            pass

    @staticmethod
    def exit(lilly, e):
        lilly.jumping = 0
        lilly.in_sky = 1
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame + 18 * Jump_ACTION_per_TIME*handle_framework.frame_time) % 18

        lilly.y += 0.5 * (lilly.jump_vel + lilly.jump_vel) * (JUMP_TIME * handle_framework.frame_time)

        lilly.jump_vel += GRAVITY * (JUMP_TIME * handle_framework.frame_time)

        lilly.x += lilly.dir * JUMP_SPEED_PPS * 1 * handle_framework.frame_time


    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageJump.clip_draw(int(lilly.frame) * 128, 0, 128, 128,lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)
        elif lilly.face_dir == 1:
            lilly.imageJump.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)




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

        if 120 < lilly.y and lilly.in_sky == 1:
            lilly.y += GRAVITY * handle_framework.frame_time * JUMP_SPEED_PPS

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageCrawl.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)
        elif lilly.face_dir == 1:
            lilly.imageCrawl.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.cx, lilly.cy, LILLY_SIZE,LILLY_SIZE)



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

