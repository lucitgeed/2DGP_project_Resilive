import math

from pico2d import load_image, draw_rectangle, get_canvas_width, get_canvas_height, clamp, delay, load_music, load_wav

import game_world
import handle_framework
import mode_gameover

#set scroll speed
SCROLL_SPEED_NEAR = 100
SCROLL_SPEED_MIDDLE = 50


# set frame flip speed
TIME_per_WATER_ACTION = 2
WATER_ACTION_per_TIME = 1.0 / TIME_per_WATER_ACTION

TIME_per_PIPE_ACTION= 1
PIPE_ACTION_per_TIME = 1.0 / TIME_per_PIPE_ACTION


#=============
class Ground_One:
    image = None
    def __init__(self, lilly):
        if Ground_One.image == None:
#            Ground_One.image = load_image("stage1_ground-Sheet.png")
            Ground_One.image = load_image("tg-Sheet.png")

        self.width, self.height = self.image.w, self.image.h

        self.lilly = lilly

        self.camera_left = 0
        self.camera_bottom = 0

        ####
        self.canvas_w = get_canvas_width()
        self.canvas_h = get_canvas_height()
        ###


    def update(self):
        self.camera_left = clamp(0,
                                int(self.lilly.x) - self.canvas_w // 2,
                                self.width - self.canvas_w - 1
                                )
        self.camera_bottom = clamp(0,
                                int(self.lilly.y) - self.canvas_h // 2,
                                self.height - self.canvas_h - 1
                                )
        pass

    def handle_event(self):pass

    def draw(self):
        self.image.clip_draw_to_origin(
            self.camera_left, self.camera_bottom,
            self.canvas_w, self.canvas_h,
            0, 0
            )

        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_boundingbox(self):
        return (self.width-8000, self.height-550,self.width, self.height-533)

    def handle_self_collision(self, crashgroup, other):
        pass




#=============
class Background1:
    def __init__(self):
        self.image = load_image('background1.png')
        self.bgm = load_music('stage1_bgm.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
        pass

    def draw(self):
        self.image.clip_draw(0,0,800,540,
                             400,300,
                             800,600)


    def update(self):pass


#=============
class PipeStrong:
    def __init__(self, x, y, sizex,sizey):
        self.x, self.y = x, y
        self.sizex = sizex
        self.sizey = sizey
        self.cx, self.cy = 0, 0

        self.image = load_image('pipe-Sheet.png')

    def update(self):
        self.cx = self.x - self.groundcam.camera_left
        self.cy = self.y - self.groundcam.camera_bottom
        pass

    def handle_event(self):pass

    def draw(self):
        self.image.clip_draw(0,0,128,128,
                             self.cx,self.cy, self.sizex, self.sizey)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam
    #--------------------------
    def get_boundingbox(self):
        return (self.cx - self.sizex/4 +10, self.cy+ self.sizey/8 ,
                self.cx + self.sizex//4 - 5, self.cy + self.sizey/9)

    def handle_self_collision(self, crashgroup, other):pass



class PipeWeak:
    def __init__(self, x, y, sizex,sizey):
        self.x, self.y = x, y
        self.sizex = sizex
        self.sizey = sizey
        self.cx, self.cy = 0, 0
        self.collapse = 0

        self.image = load_image('weakpipe.png')

    def update(self):
        self.cx = self.x - self.groundcam.camera_left
        self.cy = self.y - self.groundcam.camera_bottom

    def handle_event(self):pass

    def draw(self):
        self.image.clip_draw(0,0,128,128,
                             self.cx,self.cy, self.sizex, self.sizey)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam
    #--------------------------
    def get_boundingbox(self):
        return (self.cx - self.sizex/4 +10, self.cy + self.sizey/8,
                self.cx + self.sizex//4 - 5, self.cy + self.sizey/7)

    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:pipe':
            PIPE  = PipeAbouttoCollapse(self.x,self.y,self.sizex,self.sizey)
            PIPE.get_GF_cam_info(self.groundcam)
            game_world.add_object(PIPE,4)
            game_world.add_collision_info('lilly:pipe_abouttoCOLLAPSE', None, PIPE)
            game_world.remove_objt(self)
        pass




class PipeAbouttoCollapse:
    def __init__(self, x, y, sizex,sizey):
        self.x, self.y = x, y
        self.sizex = sizex
        self.sizey = sizey
        self.cx, self.cy = 0, 0
        self.frame = 0

        self.image = load_image('weakpipe-Sheet.png')

    def update(self):
        self.cx = self.x - self.groundcam.camera_left
        self.cy = self.y - self.groundcam.camera_bottom

        self.frame = (self.frame + 9 * PIPE_ACTION_per_TIME * handle_framework.frame_time
                      * 0.3) % 9

    def handle_event(self):pass

    def draw(self):
        self.image.clip_draw(int(self.frame)*128,0,128,128,
                             self.cx,self.cy, self.sizex, self.sizey)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam
    #--------------------------
    def get_boundingbox(self):
        return (self.cx - self.sizex/4 +10, self.cy + self.sizey/8,
                self.cx + self.sizex//4 - 5, self.cy + self.sizey/7)

    def handle_self_collision(self, crashgroup, other):
        pass








class PipeCollapse:
    def __init__(self, x, y, sizex,sizey):
        self.x, self.y = x, y
        self.sizex = sizex
        self.sizey = sizey
        self.cx, self.cy = 0, 0

        self.image = load_image('pipe-Sheet.png')

    def update(self):
        self.cx = self.x - self.groundcam.camera_left
        self.cy = self.y - self.groundcam.camera_bottom


    def handle_event(self):pass

    def draw(self):
        self.image.clip_draw(256,0,128,128,
                             self.cx,self.cy, self.sizex, self.sizey)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam
    #--------------------------
    def get_boundingbox(self):
        return (self.cx - self.sizex/4 +10, self.cy + self.sizey/8,
                self.cx + self.sizex//4 - 5, self.cy + self.sizey/7)

    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:pipe':
            self.collapse += 1
            if self.collapse == 2:
                pass
            pass
        pass




#=============
class ObstacleWater:
    image = None
    def __init__(self, lilly, x, y, sizex):
        self.frame = 0
        self.x, self.y = x, y
        self.lilly = lilly
        self.sizex = sizex

        self.cx, self.cy = 0,0

        if ObstacleWater.image == None:
            ObstacleWater.image = load_image("obstacle_water-Sheet.png")

    def update(self):
        self.cx = self.x - self.groundcam.camera_left
        self.cy = self.y - self.groundcam.camera_bottom
#        game_world.update()
        pass

    def handle_event(self):pass

    def draw(self):
        self.frame = (self.frame + 5 * WATER_ACTION_per_TIME * handle_framework.frame_time) % 5

        self.image.clip_draw(int(self.frame) * 128, 0, 128, 128, self.cx, self.cy, self.sizex, 128)

        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_boundingbox(self):
        return (self.cx-self.sizex/2+9, self.cy-64,self.cx+self.sizex//2-10, self.cy+23)

    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:water':
            game_world.remove_collision_objt(self)

            drowned = Drown(self.lilly,self.cy)
            game_world.add_object(drowned, 5)
        pass
    #--------------------------
    def get_GF_cam_info(self, groundcam):
        self.groundcam = groundcam



class Drown:
    image = None
    water_sound = None
    def __init__(self,lilly,y):
        if Drown.image == None:
            Drown.image = load_image("lilly_drown-Sheet.png")

        self.frame = 0
        self.lilly = lilly
        self.y = y

        if not Drown.water_sound:
#            Drown.water_sound = load_wav('watersound.wav')
#            Drown.water_sound.set_volume(20)
            pass


    def update(self):
#        self.water_sound.play()
        pass

    def handle_event(self, event):pass

    def draw(self):
        if int(self.frame) == 14:
            handle_framework.change_mode(mode_gameover)
            pass

        self.frame = (self.frame + 15 * WATER_ACTION_per_TIME * handle_framework.frame_time) % 15
        delay(0.02)

        if self.lilly.face_dir == -1:
            self.image.clip_draw(int(self.frame)*128,0, 128,128, self.lilly.cx+64, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * 128, 0, 128, 128, 0, 'h', self.lilly.cx+64, self.y,128,128)
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

    def handle_self_collision(self, crashgroup, other):
        if crashgroup == 'lilly:shift_1to2':
            game_world.remove_collision_objt(self)
            pass
