from ast import Param

from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, delay

import handle_framework
from StateMachine import*



PIXEL_per_METER = (10.0 / 1)      # 1pixel = 10cm
# set lilly speed
RUN_SPEED_KM_per_H = 17.0
RUN_SPEED_M_per_M = (RUN_SPEED_KM_per_H * 1000.0 / 60.0)
RUN_SPEED_M_per_S = RUN_SPEED_M_per_M / 60.0
RUN_SPEED_PPS = RUN_SPEED_M_per_S * PIXEL_per_METER

WALK_SPEED_KM_per_H = 6.5
WALK_SPEED_M_per_M = (WALK_SPEED_KM_per_H * 1000.0 / 60.0)
WALK_SPEED_M_per_S = WALK_SPEED_M_per_M / 60.0
WALK_SPEED_PPS = WALK_SPEED_M_per_S * PIXEL_per_METER
# set frame flip speed
TIME_per_Idle_ACTION = 0.8
Idle_ACTION_per_TIME = 1.0 / TIME_per_Idle_ACTION

TIME_per_Walk_ACTION = 0.8
Walk_ACTION_per_TIME = 1.0 / TIME_per_Walk_ACTION

TIME_per_Run_ACTION = 0.6
Run_ACTION_per_TIME = 1.0 / TIME_per_Run_ACTION





class Lilly:
    image = None

    def __init__(self):
        self.x, self.y = 50,80
        if Lilly.image == None:
            Lilly.imageIdle = load_image("lilly_idle_Sheet.png")
            Lilly.imageRun = load_image("lilly_run_Sheet.png")
            Lilly.imageJump = load_image("lilly_jump-Sheet.png")
            Lilly.imageWalk = load_image("lilly_walk_Sheet.png")

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle:{right_down:Walk, right_up:Walk, left_down:Walk, left_up:Walk, shift_down:Idle,
                      space_down:Jump},
                Walk:{right_down:Idle, right_up:Idle, left_down:Idle, left_up:Idle,
                      shift_down:Run,

                      jump_whenMoving:Jump},

                Run:{shift_up:Walk, right_up:Idle, left_up:Idle,
                     right_down:Run, left_down:Run,
                     jump_whenMoving:Jump},
                Jump:{landed_whenIdle:Idle, landed_whenWalk:Walk, landed_whenRun:Run,
                      space_down:Jump, right_down:Jump, left_down:Jump},
                Caught:{}
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_events(
            ('Input', event)
        )

    def draw(self):
        self.state_machine.draw()



###########
class Idle:
    @staticmethod
    def enter(lilly, e):
        if start_event(e) or  right_up(e) or left_down(e):
            lilly.face_dir = 1
        elif left_up(e) or right_down(e):
            lilly.face_dir = -1

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
            lilly.imageIdle.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 70,70)
        elif lilly.face_dir == -1:
            lilly.imageIdle.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128,
                                                0,'h', lilly.x, lilly.y, 70,70)




class Walk:
    @staticmethod
    def enter(lilly, e):
        if right_down(e) or left_up(e):
            lilly.face_dir = 1
            lilly.dir = 1
        elif left_down(e) or right_up(e):
            lilly.face_dir = -1
            lilly.dir = -1

    @staticmethod
    def exit(lilly,e):
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame+ 10 * Walk_ACTION_per_TIME * handle_framework.frame_time) % 10

        if 25 <= lilly.x <= 800 - 25:
            lilly.x += lilly.dir * WALK_SPEED_PPS * handle_framework.frame_time
        elif lilly.x < 25:
            lilly.x = 25
        elif lilly.x > 800 - 25:
            lilly.x = 800 - 25
#        delay(0.04)

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageWalk.clip_draw(int(lilly.frame)*128,0, 128,128, lilly.x, lilly.y, 70,70)
        elif lilly.face_dir == 1:
            lilly.imageWalk.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0,'h', lilly.x, lilly.y, 70,70)




class Run:
    @staticmethod
    def enter(lilly, e):
        if shift_down(e):      #????????????
            if lilly.face_dir == 1:
                lilly.dir = 1
            elif lilly.face_dir == -1:
                lilly.dir = -1

    @staticmethod
    def exit(lilly, e):
        pass

    @staticmethod
    def do(lilly):
        lilly.frame = (lilly.frame+ 8* Run_ACTION_per_TIME * handle_framework.frame_time) % 8

        if 25 <= lilly.x <= 800-25:
            lilly.x += lilly.dir * RUN_SPEED_PPS * handle_framework.frame_time
        elif lilly.x < 25:
            lilly.x = 25
        elif lilly.x > 800-25:
            lilly.x = 800-25

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageRun.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 70,70)
        elif lilly.face_dir == 1:
            lilly.imageRun.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 70,70)




class Jump:
    @staticmethod
    def enter(lilly, e):
        if space_down(e):
            lilly.dir = 0
        elif jump_whenMoving(e) or right_down(e):
            lilly.face_dir = 1
            lilly.dir = 3
        elif jump_whenMoving(e) or left_down(e):
            lilly.face_dir = -1
            lilly.dir = -3

        lilly.frame = 0

        highest = 0
        temp = lilly.y

    @staticmethod
    def exit(lilly, e):
        pass

    @staticmethod
    def do(lilly):
        startx, starty = lilly.x, lilly.y
        finishx, finishy = lilly.x + 3, lilly.y
        sx,sy = startx,starty+100
        fx,fy = finishx,finishy+100

#        lilly.frame = (lilly.frame + 1) % 18

        for i in range(0, 100,5):
            lilly.frame = (lilly.frame + 1) % 18

            t = i/100
            Ax = (1-t)*startx + t * sx
            Ay = (1-t)*starty + t * sy
            Bx = (1-t)*finishx + t * fx
            By = (1-t)*finishy + t * fy
            print(f'                    Ax is {Ax}')


            if 25 <= lilly.x <= 800 - 25:
                lilly.x = (1-t) * Ax + t * Bx
            elif lilly.x < 25:
                lilly.x = 25
            elif lilly.x > 800 - 25:
                lilly.x = 800 - 25

            if 50 <= lilly.y <= 550:
                lilly.y = (1-t) * Ay + t * By
            elif lilly.y < 50:
                lilly.y =50
            elif lilly.y > 550:
                lilly.y = 550
        delay(0.06)

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageJump.clip_draw(int(lilly.frame) * 128, 0, 128, 128, lilly.x, lilly.y, 70,70)
        elif lilly.face_dir == 1:
            lilly.imageJump.clip_composite_draw(int(lilly.frame) * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 70,70)




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
