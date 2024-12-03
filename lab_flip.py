import pico2d
from pico2d import load_image, open_canvas, close_canvas, clear_canvas, update_canvas, delay

TIME_per_WATER_ACTION = 2
WATER_ACTION_per_TIME = 1.0 / TIME_per_WATER_ACTION

global image, frame



open_canvas()

image = load_image("lilly_drown-Sheet.png")
frame = 0

while True:
    clear_canvas()
    frame = (frame + 15 * WATER_ACTION_per_TIME ) % 15

#    image.clip_draw(int(frame) * 128, 0,
#                         128, 128,
#                         400,300)
    image.clip_composite_draw(int(frame) * 128, 0, 128, 128, 0, 'v', 400,300, 128, 128)
    update_canvas()
    delay(0.4)
    pass


close_canvas()