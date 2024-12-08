import math
import random

from pico2d import load_image, draw_rectangle

import handle_framework
from behavior_tree import BehaviorTree, Action, Condition, Sequence, Selector

PIXEL_per_METER = 10.0 / 1
#set eye speed
EYE_SPEED_MPS = 25
EYE_SPEED_PPS = EYE_SPEED_MPS * PIXEL_per_METER


TIME_per_EYE_ACTION = 2
EYE_ACTION_per_TIME = 1.0 / TIME_per_EYE_ACTION



class Eyes:
    image = None
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
    def set_target(self, x = None, y = None):
        self.tx, self.ty = x, y
        return BehaviorTree.SUCCESS
        pass
    def chase_target(self, r = 1):
        self.dir = math.atan2(self.ty - self.cy,self.tx - self.cx)
        distance = EYE_SPEED_PPS * handle_framework.frame_time
        self.x += distance * math.cos(self.dir)
        self.y += distance * math.sin(self.dir)

        if self.distance_less_than(self.tx,self.ty, self.cx,self.cy, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        pass

    def distance_less_than(self, x1,x2,y1,y2,r):
        distance2 = (x1 -x2) **2 + (y1-y2)**2
        return distance2 < (PIXEL_per_METER * r)**2
        pass

    #=================
    def build_behavior_tree(self):
        # 1. Idle 상태
        move_randomly = Action('Move Randomly', self.set_random_location)
        check_collision = Condition('Check Collision with Lilly', self.check_coll_with_lilly)
        idle_sequence = Sequence('Idle', move_randomly, check_collision)

        # 2. Aggro 상태
        follow_lilly = Action('Follow Lilly', self.chase_target)
        is_hidden = Condition('Is Lilly Hidden?', self.is_lilly_hidden)

        # 숨음 -> 1초 동안 릴리를 찾고 Idle로 복귀
        search_lilly = Action('Search Lilly for 1 Second', self.search_lilly)
        return_to_idle = Action('Return to Idle', self.return_to_idle)
        hidden_sequence = Sequence('Hidden', search_lilly, return_to_idle)

        # 숨지 못함 -> Kill 상태로 전환
        enter_kill_state = Action('Enter Kill State', self.enter_kill_state)
        not_hidden_selector = Selector('Not Hidden', hidden_sequence, enter_kill_state)
        aggro_sequence = Sequence('Aggro', follow_lilly, is_hidden, not_hidden_selector)

        # 3. Kill 상태
        enlarge = Action('Enlarge Eyes', self.enlarge)
        start_kill_timer = Action('Start Kill Timer', self.start_kill_timer)
        lilly_dies = Action('Lilly Dies', self.lilly_dies)
        kill_sequence = Sequence('Kill', enlarge, start_kill_timer, lilly_dies)

        # 최상위 Selector
        root = Selector('Root', idle_sequence, aggro_sequence, kill_sequence)

        self.btree = BehaviorTree(root)
        pass
    #=================
    # #=================

    def set_random_location(self):
        self.tx, self.xy = random.randint(100,1280 - 100), random.randint(100, 1024 - 100)
        return BehaviorTree.SUCCESS
        pass

    def check_coll_with_lilly(self):
        if self.collide_lilly == 1:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def is_lilly_hidden(self):
        if self.lilly.hidden == 1:
            self.kill_timer = 0
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def search_lilly(self):
        self.search_time += handle_framework.frame_time
        if self.search_time >= 1.0:
            self.search_time = 0
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING



    def return_to_idle(self):
        self.state = 'Idle'
        self.size = random.randint(100,200)
        return BehaviorTree.SUCCESS

    def enter_kill_state(self):
        self.state = 'Kill'
        return BehaviorTree.SUCCESS

    def enlarge(self):
        if self.size < 300:
            self.size += 25 *handle_framework.frame_time
            return BehaviorTree.RUNNING
        return BehaviorTree.SUCCESS

    def start_kill_timer(self):
        if self.lilly.hidden == 0:
            self.kill_timer += handle_framework.frame_time
            if self.kill_timer >= 3.0:
                return BehaviorTree.SUCCESS
            return BehaviorTree.RUNNING
        else:
            self.kill_timer = 0
            return BehaviorTree.FAIL


    def lilly_dies(self):
        self.lilly.is_alive = False
        return BehaviorTree.SUCCESS




    #=================
    # =================
    def get_boundingbox(self):
        return (self.cx-200, self.cy-500, self.cx+200,self.cy+500)
        pass
    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:eye':
            self.collide_lilly = 1
        pass

    #------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam