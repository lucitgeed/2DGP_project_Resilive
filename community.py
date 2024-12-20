import random
from pico2d import load_image, draw_rectangle

import handle_framework
import lilly
from StateMachine import StateMachine, spot_lilly
from lilly import Caught

PIXEL_per_METER = 10.0 / 1
# set community speed
IDLE_SPEED_KMPH = random.uniform(6.0, 11.0)
IDLE_SPEED_MPS = (IDLE_SPEED_KMPH * 1000.0 / 60.0) / 60.0
IDLE_SPEED_PPS = IDLE_SPEED_MPS * PIXEL_per_METER

CHASE_SPEED_KMPH = 16.0      #조금 빠른가?
CHASE_SPEED_MPS = (CHASE_SPEED_KMPH*1000.0 / 60.0) / 60.0
CHASE_SPEED_PPS = CHASE_SPEED_MPS * PIXEL_per_METER

TryAttack_SPEED_MPS = 13
TryAttack_SPEED_PPS = TryAttack_SPEED_MPS * PIXEL_per_METER



# for frame flip speed
TIME_per_Idle_ACTION = 0.9
Idle_ACTION_per_TIME = 1.0 / TIME_per_Idle_ACTION

TIME_per_TryAttack_ACTION = 1
TryAttack_ACTION_per_TIME = 1.0 / TIME_per_TryAttack_ACTION




class Community:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50,750), random.randint(200,300)
        self.face_dir = random.choice([-1,1])

        if Community.image == None:
            Community.imageIdle = load_image("community_idle_Sheet.png")
            Community.imageChase = load_image("community_chase-Sheet.png")
            Community.imageTryAttack = load_image("community_tryattack-Sheet.png")

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)

        self.state_machine.set_transitions(
            {
                Idle:{spot_lilly:Chase},
                Chase:{}
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self):
        pass

    def draw(self):
        self.state_machine.draw()

        draw_rectangle(*self.get_boundingbox())
        draw_rectangle(*self.get_aggrobox())

    #==================
    def get_boundingbox(self):
        return (self.x-40, self.y-40, self.x+40,self.y+35)

    def get_aggrobox(self):
        if self.face_dir == 1:
            return (self.x-50, self.y-90, self.x+110,self.y+110)
        else:
            return (self.x-110, self.y-90, self.x+50,self.y+110)
    #------------------------
    def handle_self_collision(self,crashgroup, other):
        if crashgroup == 'lilly:community':
            pass
        if crashgroup == 'lilly:cmity_aggro':
            self.state_machine.start(Chase)
            pass
        if crashgroup == 'lilly:cmity_attack':
            self.state_machine.start(TryAttack)
        pass



###############
class Idle:
    @staticmethod
    def enter(cmity,event):
        cmity.frame = (random.randint(0, 21))

    @staticmethod
    def exit(cmity, e):
        pass

    @staticmethod
    def do(cmity):
        cmity.frame = (cmity.frame + 7 * Idle_ACTION_per_TIME * handle_framework.frame_time) % 7

        cmity.x += cmity.face_dir * IDLE_SPEED_PPS * handle_framework.frame_time
        if cmity.x < 25:
           cmity.face_dir = 1
        elif cmity.x > 800 - 25:
            cmity.face_dir = -1

    @staticmethod
    def draw(cmity):
        if cmity.face_dir == 1:
            cmity.imageIdle.clip_composite_draw(int(cmity.frame) * 128, 0, 128, 128, 0,'h', cmity.x, cmity.y, 70,70)
        elif cmity.face_dir == -1:
            cmity.imageIdle.clip_draw(int(cmity.frame) * 128, 0, 128, 128, cmity.x, cmity.y, 70, 70)



class Chase:
    @staticmethod
    def enter(cmity,e):
        cmity.frame = 0
        pass
    @staticmethod
    def exit(cmity, e):
        pass
    @staticmethod
    def do(cmity):
        cmity.frame = (cmity.frame + 7 * Idle_ACTION_per_TIME * handle_framework.frame_time) % 7
        cmity.x += cmity.face_dir * CHASE_SPEED_PPS * handle_framework.frame_time

        if cmity.x < 25:
            cmity.face_dir = 1
        elif cmity.x > 800 - 25:
            cmity.face_dir = -1

        pass
    @staticmethod
    def draw(cmity):
        if cmity.face_dir == 1:
            cmity.imageChase.clip_composite_draw(int(cmity.frame) * 128, 0, 128, 128, 0,'h', cmity.x, cmity.y, 70,70)
        elif cmity.face_dir == -1:
            cmity.imageChase.clip_draw(int(cmity.frame) * 128, 0, 128, 128, cmity.x, cmity.y, 70, 70)
        pass



class TryAttack:
    @staticmethod
    def enter(cmity, e):
        cmity.frame = 0

#        p3x, p3y = lilly.x, lilly.y
#        p1x, p1y = cmity.x, cmity.y
#        p2x, p2y = (lilly.x + cmity.x)/2, (lilly.y+cmity.y)*2

        pass
    @staticmethod
    def exit(cmity, e):
        pass
    @staticmethod
    def do(cmity):
        cmity.frame = (cmity.frame + 11 * TryAttack_ACTION_per_TIME * handle_framework.frame_time) % 11

        for i in range(0,100):
            t = i / 100
#            cmity.x = (2*t**2 - 3*t + 1) * p1x + (-4*t**2 + 4*t) * p2x + (2*t**2 - t) * p3x
#            cmity.y = (2*t**2 - 3*t + 1) * p1y + (-4*t**2 + 4*t) * p2y + (2*t**2 - t) * p3y

    @staticmethod
    def draw(cmity):
        if cmity.face_dir == 1:
            cmity.imageTryAttack.clip_composite_draw(int(cmity.frame) * 128, 0, 128, 128, 0,'h', cmity.x, cmity.y, 70,70)
        elif cmity.face_dir == -1:
            cmity.imageTryAttack.clip_draw(int(cmity.frame) * 128, 0, 128, 128, cmity.x, cmity.y, 70, 70)
    pass


class AttackSuccess:
    pass