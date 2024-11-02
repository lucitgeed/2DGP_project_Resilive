from pico2d import load_image
from StateMachine import State_Machine



class Lilly:
    image = None

    def __init__(self):
        self.x, self.y = 50,90  #테스트를 위한 임시값
        self.frame = 0
#        self.action = 0
        self.dir = 0

        if Lilly.image == None:
            Lilly.image = load_image("lilly_idle_Sheet.png")

        self.state_machine = State_Machine(self)
        self.state_machine.start(Idle)

    def update(self):
        self.frame = (self.frame+1) % 5
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128,0, 128,128, self.x,self.y)




class Idle:
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


