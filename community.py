import random
from pico2d import load_image
from StateMachine import StateMachine


class Community:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50,750), random.randint(200,650)

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



#####
class Idle:
    @staticmethod
    def enter(cmity,event):
        cmity.frame = (random.randint(0, 7))

        pass

    @staticmethod
    def exit(cmity):
        pass

    @staticmethod
    def do(cmity):
        cmity.frame = (cmity.frame + 1) % 7
        cmity.x = cmity.x + random.randint(-20, 20)

    @staticmethod
    def draw(cmity):
        cmity.imageIdle.clip_draw(int(cmity.frame) * 128, 0, 128, 128, cmity.x, cmity.y, 70, 70)
        #임시위치
        #랜덤값 추가로 설정할 것





class Find:
    pass


class Chase:
    pass


class Jump:
    pass



class TryAttack:
    pass


class AttackSuccess:
    pass


#class 충돌:
#    pass