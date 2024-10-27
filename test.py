from pico2d import*

open_canvas()

community = load_image("community_idle_Sheet.png")

frame = 0
for x in range(0,100):
    clear_canvas()
    community.clip_draw(frame*128,0, 128,128, 400,300) 
    print("clipdraw")
    update_canvas()
    print("update")
    frame = (frame+1) %7
    print("%7")
    delay(0.1)

close_canvas()

