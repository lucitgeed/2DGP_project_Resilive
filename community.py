from random import random

from pico2d import load_image


class Community:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(50,750, 50), random.randint(200,650, 100)
        self.frame= random.randint(0,7)
        if Community.image == None:
            Community.image = load_image("community_idle_Sheet.png")

    def update(self):
        self.frame = (self.frame+1) %7
        self.x = self.x + random.randint(-10, 10)

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128,0, 128,128, self.x, self.y, 70,70)
        #임시위치
        #랜덤값 추가로 설정할 것



class Idle:
    pass


class Find:
    pass


class Chase:
    pass


#class 충돌:
#    pass