from random import random

from pico2d import*


class Lilly:
    image = None

    def __init__(self):
        self.x, self.y = 50,90  #테스트를 위한 임시값
        
        self.frame = 0
        if Lilly.image == None:
            Lilly.image = load_image("lilly_idle_Sheet.png")

    def update(self):
        self.frame = (self.frame+1) % 5

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame*128,0, 128,128, self.x,self.y)
        



class Eyes:
    pass






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



        








##
def reset_world():
    global world
    global running
    
    global lilly
    global group
    
    running = True
    world = []

    lilly = Lilly()
#    community = Community()
    group = [Community() for i in range(5)]

    world.append(lilly)
    world += group
    pass


def update_world():
    for objt in world:
        objt.update()
    pass


def render_world():
    clear_canvas()

    for objt in world:
        objt.draw()
        
    update_canvas()
    pass



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            lilly.handle_event(event)






##
open_canvas()

reset_world()

while running:
    
    update_world()
    render_world()
    delay(0.09)
    pass



close_canvas()
