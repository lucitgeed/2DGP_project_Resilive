import random

from pico2d import load_image, draw_rectangle


PIXEL_per_METER = 10.0 / 1
#set eyepupil speed
IDLE_SPEED_MPS = 4
IDLE_SPEED_PPS = IDLE_SPEED_MPS * PIXEL_per_METER



class Eyes:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50, 750), random.randint(350, 550)
        self.size = random.randint(60, 120)
        self.dir = random.choice([-1,1])

        if Eyelid.image == None:
            Eyelid.image = load_image('eyelid_blink_Sheet.png')
            Eyelid.eyesimage = load_image('eyes-Sheet.png')
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