import pico2d
from pico2d import load_image, open_canvas, close_canvas, clear_canvas, update_canvas, delay

TIME_per_WATER_ACTION = 2
WATER_ACTION_per_TIME = 1.0 / TIME_per_WATER_ACTION

global image, frame



open_canvas()

#image = load_image("test3.png")
frame = 0

#cnt = 0

while True:
    if 0<=self.cnt <10:
        image = load_image("test1.png")
    if 10<=cnt<20:
        image = load_image("test2.png")
    if 20<=cnt <30:
        image = load_image("test3.png")


    clear_canvas()
    print(f'cnt = {cnt}')
    print(f'cnt = {image}')

#    cnt = cnt+1

    image.clip_draw(int(frame) * 512, 0, 512,256, 400,300)
    frame = (frame + 1 ) % 10
    delay(0.4)
    update_canvas()
#
    pass


close_canvas()