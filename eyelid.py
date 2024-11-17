import random

from pico2d import load_image, draw_rectangle

import handle_framework
from StateMachine import StateMachine

#set eyelid frame flip speed
TIME_per_BLINK_ACTION = 2.5
BLINK_ACTION_per_TIME = 1.0 / TIME_per_BLINK_ACTION




class Eyelid:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50, 750), random.randint(350, 550)
        self.size = random.randint(60, 120)
        self.dir = random.choice([-1,1])

        if Eyelid.image == None:
            Eyelid.image = load_image('eyelid_blink_Sheet.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start(APPEAR)
        self.state_machine.set_transitions(
            {

            }
        )

        pass


    def update(self):
        self.state_machine.update()
        pass

    def handle_event(self):pass

    def draw(self):
        self.state_machine.draw()

        draw_rectangle(*self.get_boundingbox())
        pass

    #=================
    def get_boundingbox(self):
        return (self.x-self.size/3, self.y-self.size/3, self.x+self.size/3,self.y+self.size/3)
        pass

    #------------------------
    def handle_self_collision(self, crashgroup, other):
        pass



##################
class APPEAR:
    @staticmethod
    def enter(lid, event):
        lid.frame = 0
        pass

    @staticmethod
    def exit(lid):
        pass

    @staticmethod
    def do(lid):
        lid.frame = (lid.frame + 18 * BLINK_ACTION_per_TIME * handle_framework.frame_time) % 18
        pass


    @staticmethod
    def draw(lid):
        if lid.dir == 1:
            lid.image.clip_draw(int(lid.frame) * 128, 0, 128, 128, lid.x, lid.y, lid.size,lid.size)
        elif lid.dir == -1:
            lid.image.clip_composite_draw(int(lid.frame) * 128,0, 128,128, 0,'h', lid.x,lid.y, lid.size,lid.size)

