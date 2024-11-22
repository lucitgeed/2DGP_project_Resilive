from tkinter import image_names

from pico2d import load_image, draw_rectangle

import game_world


class Ground_One:
    image = None
    def __init__(self):
        self.x, self.y = 400,300
        if Ground_One.image == None:
            Ground_One.image = load_image("stage_1-Sheet.png")

    def update(self):
#        game_world.update()
        pass

    def handle_event(self, event):pass

    def draw(self):
#        self.image.clip_draw(0 * 128, 0, 128, 22, self.x, self.y, 300,30)
        self.image.draw(400, 300, 6000,600)
        draw_rectangle(*self.get_boundingbox())

    #------------------------
    def get_boundingbox(self):
        return (self.x-400, self.y-300,self.x+400, self.y-225)
    def get_aggrobox(self):
        return (self.x-400, self.y-300,self.x+400, self.y-225)

    def handle_self_collision(self, crashgroup, other):
        pass



class StageOne:
    def __init__(self):
        self.image = load_image('stage_one_back.png')

    def draw(self):
        self.image.draw(400,300, 1200,900)

    def update(self):
        pass

#########################################################
class Ground_two:
    pass





class Ground_three:
    pass
