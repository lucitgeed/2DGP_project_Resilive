import random

from pico2d import load_image, draw_rectangle

import handle_framework
from StateMachine import StateMachine

PIXEL_per_METER = 10.0 / 1
#set eyepupil speed
IDLE_SPEED_MPS = 4
IDLE_SPEED_PPS = IDLE_SPEED_MPS * PIXEL_per_METER


class Eyepupil:
    image = None

    def __init__(self,lidx, lidy):
        self.size = random.randint(10,40)
        self.dir = random.choice([-1,1])
        self.frame = 0
        self.x, self.y = random.randint(lidx - self.size ,750),random.randint(350,550)

        if Eyepupil.image == None:
            Eyepupil.imageIDLE = load_image('eyepupil_idle.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start(IDLE)
        self.state_machine.set_transitions(
            {

            }
        )


    def update(self):
        self.state_machine.update()

    def handle_event(self): pass

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_boundingbox())
        draw_rectangle(*self.get_aggrobox())
        pass


    #=================
    def get_boundingbox(self):
        return (self.x - self.size / 3, self.y - self.size / 3, self.x + self.size / 3, self.y + self.size / 3)
        pass

    def get_aggrobox(self):
        return (self.x - self.size *3, self.y - self.size *6, self.x + self.size *3, self.y + self.size *2)
        pass

    #------------------------
    def handle_self_collision(self,crashgroup, other):

        pass




##################

class IDLE:
    @staticmethod
    def enter(pupil, event):
        pass

    @staticmethod
    def exit(pupil):
        pass

    @staticmethod
    def do(pupil):
        pupil.x += pupil.dir * IDLE_SPEED_PPS * handle_framework.frame_time
        pupil.y += pupil.dir*IDLE_SPEED_PPS * handle_framework.frame_time

        pass

    @staticmethod
    def draw(pupil):
        pupil.imageIDLE.clip_draw(int(pupil.frame) * 128, 0, 128, 128, pupil.x,pupil.y, pupil.size,pupil.size)
        pass
