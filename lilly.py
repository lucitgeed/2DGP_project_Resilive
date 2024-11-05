from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, delay
from StateMachine import*


class Lilly:
    image = None

    def __init__(self):
        self.x, self.y = 50,90  #테스트를 위한 임시값

        if Lilly.image == None:
            Lilly.imageIdle = load_image("lilly_idle_Sheet.png")
            Lilly.imageRun = load_image("lilly_run_Sheet.png")
            Lilly.imageJump = load_image("lilly_jump_Sheet.png")
            Lilly.imageWalk = load_image("lilly_walk_Sheet.png")

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle:{right_down:Walk, right_up:Walk, left_down:Walk, left_up:Walk, shift_down:Idle},
                Walk:{right_down:Idle, right_up:Idle, left_down:Idle, left_up:Idle,
                      shift_down:Run},
                Run:{shift_up:Walk, right_up:Idle, left_up:Idle}


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
        delay(0.07)
        pass

    @staticmethod
    def draw(lilly):
        if lilly.face_dir == 1:
            lilly.imageIdle.clip_draw(lilly.frame * 128, 0, 128, 128, lilly.x, lilly.y, 100,100)
        elif lilly.face_dir == -1:
            lilly.imageIdle.clip_composite_draw(lilly.frame * 128, 0, 128, 128,
                                                0,'h', lilly.x, lilly.y, 100, 100)



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
        lilly.frame = (lilly.frame+1) % 10
        lilly.x += lilly.dir * 2


    @staticmethod
    def draw(lilly):
        if lilly.face_dir == -1:
            lilly.imageWalk.clip_draw(lilly.frame*128,0, 128,128, lilly.x, lilly.y, 100,100)
        elif lilly.face_dir == 1:
            lilly.imageWalk.clip_composite_draw(lilly.frame * 128, 0, 128, 128, 0,'h', lilly.x, lilly.y, 100, 100)




class Run:
    @staticmethod
    def enter(lilly, e):
        if shift_down(e):      #???????????????
            if right_down(e) or left_up(e):
                lilly.face_dir = 1
                lilly.dir = 1
            elif left_down(e) or right_up(e):
                lilly.face_dir = -1
                lilly.dir = -1

    @staticmethod
    def exit(lilly, e):
        pass

    @staticmethod
    def do(lilly, e):
        lilly.frame = (lilly.frame+1) % 10
        lilly.x += lilly.dir * 5
    @staticmethod
    def draw(lilly, e):
        if lilly.face_dir == -1:
            lilly.imageWalk.clip_draw(lilly.frame * 128, 0, 128, 128, lilly.x, lilly.y, 100, 100)
        elif lilly.face_dir == 1:
            lilly.imageWalk.clip_composite_draw(lilly.frame * 128, 0, 128, 128, 0, 'h', lilly.x, lilly.y, 100, 100)


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