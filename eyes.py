import math
import random

from pico2d import load_image, draw_rectangle, load_wav

import game_world
import handle_framework
import mode_gameover
from behavior_tree import BehaviorTree, Action, Condition, Sequence, Selector
from stagetwo_info import ThornDeath

PIXEL_per_METER = 10.0 / 1
#set eye speed
EYE_SPEED_MPS = 19
EYE_SPEED_PPS = EYE_SPEED_MPS * PIXEL_per_METER


TIME_per_EYE_ACTION = 3.5
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

        if not Eyes.eye_sound:
            Eyes.eye_sound = load_wav('eyesound.wav')
            Eyes.eye_sound.set_volume(20)
            pass


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
        if int(self.frame) == 13:
            self.frame = 13
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
        a1 = Action('Set target location', self.set_target_location)
        a3 =Action("Set Random Location", self.set_random_location)
        a2 = Action("Move to Location", self.move_to)
        Idle = Sequence('Move to random location', a3, a2)

        # 릴리를 추격하는 동작 (거리가 500 이하일 때만 실행)
        c1 = Condition('릴리와의 거리가 500이하?', self.lilly_is_near, 500)
        a4 =Action('Chase Lilly', self.chase_lilly)
        chase_lilly = Sequence('CHASE LILLY', c1, a4)

        root = cha_or_Idle = Selector('Idle이나 추적', chase_lilly,Idle)

        self.btree = BehaviorTree(root)
        pass
    #=================
    # #=================
    def move_slightly_to(self, tx, ty):
        dir = math.atan2(ty - self.y, tx - self.x)
        self.x += EYE_SPEED_PPS * handle_framework.frame_time  * math.cos(dir)
        self.y += EYE_SPEED_PPS * handle_framework.frame_time  * math.sin(dir)

    def set_random_location(self):
        self.tx, self.ty = random.randint(3000, 6000), random.randint(200, 600)
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
        if self.distance_less_than(self.lilly.x, self.lilly.y, self.x, self.y, 250):
            self.eye_sound.play()
            pass
        if self.distance_less_than(self.lilly.x, self.lilly.y, self.x, self.y, 1):
            thornd = ThornDeath(self.lilly,self.cy)
            game_world.add_object(thornd, 8)
            handle_framework.change_mode(mode_gameover)
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def set_target_location(self, x=None, y=None):
        if not x or not y:
            raise ValueError('Location should be given')
        self.tx, self.ty = x,y                          #이게 정해진 순간 해당 task 성공
        return BehaviorTree.SUCCESS

    def lilly_is_near(self, r):
        if self.distance_less_than(self.lilly.x, self.lilly.y, self.x, self.y, r):
            self.is_chasing = True
            return BehaviorTree.SUCCESS
        else:
            self.is_chasing = False
            return BehaviorTree.FAIL

    #=================
    # =================
    def get_boundingbox(self):
        return (self.cx-self.size/4, self.cy+self.size/7, self.cx+self.size/4,self.cy+self.size/6)
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