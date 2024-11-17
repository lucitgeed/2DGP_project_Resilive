from pico2d import load_image

from StateMachine import StateMachine

PIXEL_per_METER = 10.0 / 1
#set eyepupil speed
IDLE_SPEED_MPS = 0.005                              #1초에 0.5CM라고하면, 1초에 0.005M네
IDLE_SPEED_PPS = IDLE_SPEED_MPS * PIXEL_per_METER


class Eyepupil:
    image = None

    def __init__(self):

        if Eyepupil.image == None:
            Eyepupil.imageIDLE = load_image('eyepupil.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start(IDLE)
        self.state_machine.transitions(
            {

            }
        )


    def update(self):
        self.state_machine.update()

    def handle_event(self): pass

    def draw(self):
        self.state_machine.draw()
        pass


    #=================
    def get_boundingbox(self):
        pass

    def get_aggrobox(self):
        pass

    #------------------------
    def handle_self_collision(self):
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
        pass

    @staticmethod
    def draw(pupil):
        pass
