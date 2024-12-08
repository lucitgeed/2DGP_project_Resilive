import math
import random

from pico2d import load_image, draw_rectangle

import handle_framework
from behavior_tree import BehaviorTree, Action, Condition, Sequence, Selector

PIXEL_per_METER = 10.0 / 1
#set eye speed
EYE_SPEED_MPS =5
EYE_SPEED_PPS = EYE_SPEED_MPS * PIXEL_per_METER


TIME_per_EYE_ACTION = 2
EYE_ACTION_per_TIME = 1.0 / TIME_per_EYE_ACTION



class Eyes:
    image = None
    eye_sound = None
    def __init__(self,lilly, x, y):
        self.lilly = lilly
        self.x, self.y = x, y
        self.frame = 0
        self.size = random.randint(100, 200)

        self.cx, self.cy = 0, 0
        if Eyes.image == None:
#            Eyes.image = load_image('eyelid_blink_Sheet.png')
            Eyes.image = load_image('eyes-Sheet.png')


        self.state = 'appear'
        self.tx,self.ty = 0,0
        self.build_behavior_tree()


        self.collide_lilly = 0
        self.kill_timer = 0
        self.search_time = 0
        pass

    def update(self):
        self.cx = self.x - self.groundcam.camera_left
        self.cy = self.y - self.groundcam.camera_bottom
        self.frame = (self.frame + 14 * EYE_ACTION_per_TIME * handle_framework.frame_time) % 14

        self.btree.run()
        pass

    def handle_event(self):pass

    def draw(self):
        self.image.clip_draw(int(self.frame)*128,0,128,128,
                             self.cx,self.cy, self.size, self.size)
        draw_rectangle(*self.get_boundingbox())
        pass

    #=================
    #=================
    def build_behavior_tree(self):
        # 랜덤 위치 설정 후 이동
        # 랜덤 위치 설정 후 이동
        a1 = Action('Set target location', self.set_target_location)
        a3 =Action("Set Random Location", self.set_random_location)
        a2 = Action("Move to Location", self.move_to)
        Idle = Sequence('Move to random location', a3, a2)



        # 릴리를 추격하는 동작 (거리가 100 이하일 때만 실행)
        c1 = Condition('릴리와의 거리가 100이하?', self.lilly_is_near, 1000)
        a4 =Action('Chase Lilly', self.chase_lilly)
        chase_lilly = Sequence('CHASE LILLY', c1, a4)


        root = cha_or_Idle = Selector('Idle이나 추적', chase_lilly,Idle)



        c2 = Condition('릴리와 충돌했는가?', self.check_collision_with_lilly)


        self.btree = BehaviorTree(root)
        pass
        pass
    #=================
    # #=================
    def move_slightly_to(self, tx, ty):
        dir = math.atan2(ty - self.y, tx - self.x)
        self.x += EYE_SPEED_PPS * handle_framework.frame_time  * math.cos(dir)
        self.y += EYE_SPEED_PPS * handle_framework.frame_time  * math.sin(dir)

    def set_random_location(self):
        self.tx, self.ty = random.randint(3500, 3900), random.randint(300, 400)
        return BehaviorTree.SUCCESS

    def move_to(self):
        self.move_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.tx, self.ty, self.x, self.y, 5):
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def distance_less_than(self, x1, y1, x2, y2, r):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 < r ** 2

    def check_collision_with_lilly(self):
        if self.collide_lilly:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def chase_lilly(self):
        self.state = "Chase"
        self.move_slightly_to(self.lilly.x, self.lilly.y)
        if self.distance_less_than(self.lilly.x, self.lilly.y, self.x, self.y, 10):
            pass
        if self.distance_less_than(self.lilly.x, self.lilly.y, self.x, self.y, 2):
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def set_target_location(self, x=None, y=None):
        if not x or not y:
            raise ValueError('Location should be given')
        self.tx, self.ty = x,y                          #이게 정해진 순간 해당 task 성공
        return BehaviorTree.SUCCESS

    def start_kill_timer(self):
        if self.is_chasing:
            self.kill_timer += handle_framework.frame_time
            if self.kill_timer >= 3.0:  # 3초가 지나면 릴리 죽음
                self.kill_lilly()
                return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def reset_to_idle(self):
        self.state = "Idle"
        self.kill_timer = 0
        self.size = random.randint(100, 200)
        self.is_chasing = False
        return BehaviorTree.SUCCESS

    def lilly_is_near(self, r):
        if self.distance_less_than(self.lilly.x, self.lilly.y, self.x, self.y, r):
            self.is_chasing = True
            return BehaviorTree.SUCCESS
        else:
            self.is_chasing = False
            return BehaviorTree.FAIL




    def kill_lilly(self):
        print("릴리 사망!")

    def check_lilly_collision(self):
        # 충돌 처리 없이 'lilly:eye' 충돌 체크만 수행
        if self.collide_lilly:  # 릴리와 충돌 시
            print("릴리와 충돌 발생!")
            # 추격 중인 상태에서 릴리와 충돌하면 추격을 중지하고 랜덤 배회 상태로 변경
#            self.reset_to_idle()
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING


    #=================
    # =================
    def get_boundingbox(self):
        return (self.cx-self.size/2, self.cy-self.size/2, self.cx+self.size/2,self.cy+self.size/2)
        pass
    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:eye':
            self.collide_lilly = True
        else:
            self.collide_lilly = False
        print(f'            colide_lilly = {self.collide_lilly}')
        pass


    #------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam