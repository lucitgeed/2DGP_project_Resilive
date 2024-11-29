from tkinter import image_names

from pico2d import load_image, draw_rectangle, get_canvas_width, get_canvas_height, clamp, delay

import game_world
import handle_framework


# set frame flip speed
TIME_per_WATER_ACTION = 2
WATER_ACTION_per_TIME = 1.0 / TIME_per_WATER_ACTION


#=============
class Ground_One:
    image = None
    def __init__(self,lilly):
#        self.x, self.y = 400,300
        if Ground_One.image == None:
            Ground_One.image = load_image("stage_1-Sheet.png")

        self.width, self.height = self.image.w, self.image.h

        print(f"Image Width: {self.width}, Image Height: {self.height}")
        delay(0.5)


        self.canvas_w = get_canvas_width()
        self.canvas_h = get_canvas_height()

        print(f"Canvas Width: {self.canvas_w}, Canvas Height: {self.canvas_h}")


        self.lilly_x = lilly.x
        self.lilly_y = lilly.y
        print(f"Lilly X: {self.lilly_x}, Lilly Y: {self.lilly_y}")


    def update(self):
        self.window_left = clamp(0,
                                 int(self.lilly_x) - self.canvas_w // 2,
                                 self.width - self.canvas_w - 1
                                 )
        self.window_bottom = clamp(0,
                                   int(self.lilly_y) - self.canvas_h // 2,
                                   self.height - self.canvas_h - 1
                                   )

        print(f"Window Left: {self.window_left}, Window Bottom: {self.window_bottom}")

        pass

    def handle_event(self, event):pass

    def draw(self):
#        self.image.clip_draw(0 * 128, 0, 128, 22, self.x, self.y, 300,30)
#        self.image.draw(400, 300, 6000,600)
        print(f"Window Left: {self.window_left}, Window Bottom: {self.window_bottom}")
        print(f"Canvas Width: {self.canvas_w}, Canvas Height: {self.canvas_h}")

        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_w, self.canvas_h,
            0, 0
            )

#        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_boundingbox(self):
        return (self.width-400, self.height-300,self.width+400, self.height-225)
    def get_aggrobox(self):
        return (self.width-400, self.height-300,self.width+400, self.height-225)

    def handle_self_collision(self, crashgroup, other):
        pass



#=============
class StageOne:
    def __init__(self, lilly):
        self.image = load_image('stage_one_back.png')

        self.width, self.height = self.image.w, self.image.h

        self.canvas_w = get_canvas_width()
        self.canvas_h = get_canvas_height()

        self.window_left = 0
        self.window_bottom = 0

        self.lilly_x = lilly.x
        self.lilly_y = lilly.y
        pass

    def draw(self):
#        self.image.draw(400,300, 1200,900)
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_w, self.canvas_h,
            0,0
        )

    def update(self):
        self.window_left = clamp(0,
                                 int(self.lilly_x) - self.canvas_w // 2,
                                 self.width - self.canvas_w - 1
                                 )
        self.window_bottom = clamp(0,
                                   int(self.lilly_y) - self.canvas_h // 2,
                                   self.height - self.canvas_h - 1
                                   )
        pass



#=============
class ShiftObjt1:
    image = None
    def __init__(self):
        game_world.add_collision_info("lilly:shiftobjt1", None, self)

        self.x, self.y = 400,300
        if ShiftObjt1.image == None:
            ShiftObjt1.image = load_image("shift_objt1.png")

    def update(self):
#        game_world.update()
        pass

    def handle_event(self, event):pass

    def draw(self):
        self.image.draw(400, 200, 500,250)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_boundingbox(self):
        return (self.x-250, self.y-110,self.x+250, self.y+115)
    def get_aggrobox(self):
        return (self.x-250, self.y-110,self.x+250, self.y+115)

    def handle_self_collision(self, crashgroup, other):
        pass


#=============
class ObstacleWater:
    image = None
    def __init__(self):
        self.frame = 0
        self.x, self.y = 400,64
        if ObstacleWater.image == None:
            ObstacleWater.image = load_image("obstacle_water-Sheet.png")

    def update(self):
#        game_world.update()
        pass

    def handle_event(self, event):pass

    def draw(self):
        self.frame = (self.frame + 5*WATER_ACTION_per_TIME* handle_framework.frame_time)%5
        self.image.clip_draw(int(self.frame) * 128, 0, 128, 128, self.x, self.y)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_boundingbox(self):
        return (self.x-64, self.y-64,self.x+64, self.y+64)
    def get_aggrobox(self):
        return (self.x-64, self.y-64,self.x+64, self.y+64)

    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:water':
            game_world.remove_collision_objt(self)

            drowned = Drown(self.x, self.y)
            game_world.add_object(drowned, 5)
        pass



class Drown:
    image = None
    def __init__(self, x, y):
        self.frame = 0
        ############
        self.x, self.y = x, y
        ###########lilly위치에 맞춰 수정 요함
        if Drown.image == None:
            Drown.image = load_image("lilly_drown-Sheet.png")

    def update(self):pass

    def handle_event(self, event):pass

    def draw(self):
        if self.frame == 14:
            pass

        self.frame = (self.frame + 15 * WATER_ACTION_per_TIME * handle_framework.frame_time) % 15

#        if lilly.face_dir == -1:
        self.image.clip_draw(int(self.frame)*128,0,
                             128,128,
                             self.x, self.y)
#        elif lilly.face_dir == 1:
#        self.image.clip_composite_draw(int(self.frame)*128,0,
#                                       128,128,
#                                       0,'h',
#                                       self.x,self.y)

#        if mode_play.lilly.face_dir == -1:
#            Drown.image.clip_draw(int(self.frame) * 128, 0, 128, 128, self.x, self.y)
#        elif mode_play.lilly.face_dir == 1:
#            Drown.image.clip_composite_draw(int(self.frame) * 128, 0, 128, 128, 0, 'h',self.x, self.y)
        pass





#########################################################
class Ground_two:
    pass





class Ground_three:
    pass
