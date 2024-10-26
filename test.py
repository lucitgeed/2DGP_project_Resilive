from pico2d import*

open_canvas()

lilly = load_image("lilly_idle_Sheet.png")

frame = 0
for x in range(0,100):
    clear_canvas()
    lilly.clip_draw(frame*128,0, 128,128, 400,300)
    update_canvas()
    frame = (frame+1) %5
    delay(0.08)

close_canvas()

