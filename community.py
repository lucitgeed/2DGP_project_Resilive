import random
from pico2d import load_image
from StateMachine import StateMachine


class Community:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(50,750), random.randint(200,550)

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
        cmity.frame = (random.randint(0, 7))
        cmity.face_dir = (random.randint(-1,0))                     #여기서만 방향 -1은 왼쪽, 0은 오른쪽
        pass

    @staticmethod
    def exit(cmity):
        pass

    @staticmethod
    def do(cmity):
        cmity.frame = (cmity.frame + 1) % 7

        if 25 <= cmity.x <= 800 - 25:
            if cmity.face_dir == 0:
                cmity.x = cmity.x + random.randint(0, 10)
            elif cmity.face_dir == -1:
                cmity.x = cmity.x - random.randint(0, 10)
        elif cmity.x < 25:
            cmity.x = 25
            cmity.face_dir = 0
        elif cmity.x > 800 - 25:
            cmity.x = 800 - 25
            cmity.face_dir = -1

    @staticmethod
    def draw(cmity):
        if cmity.face_dir == 0:
            cmity.imageIdle.clip_composite_draw(int(cmity.frame) * 128, 0, 128, 128, 0,'h', cmity.x, cmity.y, 70,70)
        elif cmity.face_dir == -1:
            cmity.imageIdle.clip_draw(int(cmity.frame) * 128, 0, 128, 128, cmity.x, cmity.y, 70, 70)





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