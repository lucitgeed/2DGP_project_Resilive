import random
from pico2d import load_image

import handle_framework
from StateMachine import StateMachine



PIXEL_per_METER = 10.0 / 1
# set community speed
IDLE_SPEED_KMPH = random.uniform(6.0, 11.0)
IDLE_SPEED_MPS = (IDLE_SPEED_KMPH * 1000.0 / 60.0) / 60.0
IDLE_SPEED_PPS = IDLE_SPEED_MPS * PIXEL_per_METER

CHASE_SPEED_KMPH = 16.0      #조금 빠른가?
CHASE_SPEED_MPS = (CHASE_SPEED_KMPH*1000.0 / 60.0) / 60.0
CHASE_SPEED_PPS = CHASE_SPEED_MPS * PIXEL_per_METER


# for frame flip speed
TIME_per_Idle_ACTION = 0.9
Idle_ACTION_per_TIME = 1.0 / TIME_per_Idle_ACTION




class Community:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50,750), random.randint(200,550)
        self.face_dir = random.choice([-1,1])

        if Community.image == None:
            Community.imageIdle = load_image("community_idle_Sheet.png")

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
#                Idle:{find_lilly:Chase}
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self):
        pass

    def draw(self):
        self.state_machine.draw()



###########
class Idle:
    @staticmethod
    def enter(cmity,event):
        cmity.frame = (random.randint(0, 21))

    @staticmethod
    def exit(cmity):
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

    pass


class Find:
    pass

class Jump:
    pass



class TryAttack:
    pass


class AttackSuccess:
    pass


#class 충돌:
#    pass