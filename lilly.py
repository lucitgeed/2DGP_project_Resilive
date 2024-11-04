from pico2d import load_image, get_time,SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from StateMachine import*


class Lilly:
    image = None

    def __init__(self):
        self.x, self.y = 50,90  #테스트를 위한 임시값
#        self.action = 0

        if Lilly.image == None:
            Lilly.imageIdle = load_image("lilly_idle_Sheet.png")
            Lilly.imageRun = load_image("lilly_run_Sheet.png")
            Lilly.imageJump = load_image("lilly_jump_Sheet.png")
            Lilly.imageWalk = load_image("lilly_walk_Sheet.png")

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle:{right_down:Walk, right_up:Walk, left_down:Walk, left_up:Walk},
                Walk:{right_down:Idle, right_up:Idle, left_down:Idle, left_up:Idle}


            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_event(
            ('Input', event)
        )

    def draw(self):
        self.state_machine.draw()



#####
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
        lilly.frame= (lilly.frame + 1) % 5
        pass

    @staticmethod
    def draw(lilly):
        print('             idle clipdraw 시작')
        lilly.imageIdle.clip_draw(lilly.frame * 128, 0, 128, 128, lilly.x, lilly.y)
        print('             idle clipdraw 종료')



class Walk:
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




class Run:
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




class Jump:
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