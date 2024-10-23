from pico2d import*

class Community:
    image = None
    
    def _init_(self):
        self.x, self.y = 30,40
        self.frame = 0
        if Community.image == None:
            Community.image = load_image('community_idle-Sheet.png')


    def update(self):
        self.frame = (self.frame + 1) % 7
#        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*128, 0, 128, 128, self.x, self.y)
        pass



def reset_world():
    global running
    running = True

    global community
    community = Community()
    



def update_world():
    community.update()
    pass


def render_world():
    clear_canvas()
    community.draw()
    update_canvas()




open_canvas()


reset_world()



while running:
    pass


close_canvas()
