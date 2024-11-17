import random

from pico2d import load_image

from StateMachine import StateMachine

#set eyelid frame flip speed


#set pupil frame flip speed

FOUND_ACTION_PER_TIME = 1.0





class Eyelid:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50, 750), random.randint(350, 550)

        if Eyelid.image == None:
            Eyelid.image = load_image('eyelid_blink_Sheet.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start(APPEAR)
        self.state_machine.transitions(
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
class APPEAR:
    @staticmethod
    def enter(lid, event):
        pass

    @staticmethod
    def exit(lid):
        pass

    @staticmethod
    def do(lid):
        pass


    @staticmethod
    def draw(lid):
        pass


