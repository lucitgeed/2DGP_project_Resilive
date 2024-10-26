from pico2d import*


class Lilly:

    def __init__(self):
        self.x, self.y = 400,90  #테스트를 위한 임시값

        self.frame = 0
        self.image = load_image("lilly_idle_Sheet.png")
#       self.image = None

    def update(self):
        self.frame = (self.frame+1) % 5

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128,0, 128,128, self.x,self.y)
        



##
def reset_world():
    global world
    global running
    
    running = True
    world = []

    lilly = Lilly()
    world.append(lilly)

    print("lilly append")

    pass


def update_world():
    for objt in world:
        objt.update()
        print("objt")
    pass


def render_world():
    clear_canvas()
    #
    update_canvas()
    print("renderworld")




##
open_canvas()

reset_world()

while running:
    
    update_world()
#    render_world()
    delay(0.04)
    pass



close_canvas()
