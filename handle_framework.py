import time

from game_world import world

running = None
mode_stack = None



def run(mode):
    global running
    running = True

    global mode_stack
    mode_stack = [mode]
    mode.init_mode()

    global frame_time
    frame_time = 0.0
    start_time = time.time()

    while(running):
        mode_stack[-1].handle_events()
        mode_stack[-1].update()
        mode_stack[-1].draw()

        frame_time = time.time() - start_time
#        frame_rate = 1.0/ frame_time
        start_time += frame_time

    while(len(mode_stack) > 0):
        mode_stack[-1].finish()
        mode_stack.pop()
    pass


def change_mode(mode):
    global mode_stack
    if (len(mode_stack) > 0):       #
        mode_stack[-1].finish()     #모드를 끝내고,
        mode_stack.pop()            #모드를 pop
    mode_stack.append(mode)         #새로운 모드를 append
    mode.init_mode()
    pass


def push_mode(mode):
    global mode_stack
    if (len(mode_stack) > 0):
        mode_stack[-1].pause()
    mode_stack.append(mode)
    mode.init_mode()
    pass



def pop_mode():                     #현재상태를 종료하고 이전상태로 돌아가는거
    global mode_stack
    if (len(mode_stack) > 0):
        mode_stack[-1].finish()
        mode_stack.pop()

    if (len(mode_stack) > 0):
        mode_stack[-1].resume()
    pass


def quit():
    global running
    running = False
    pass


##for mode_play -> mode_menu -> mode_title -> mode_play
def back_to_frstbeginning(mode):
    global mode_stack

    while(len(mode_stack) > 0):
        print(f'{len(mode_stack)}')
        print(f'          In mode_stack : {mode_stack}')
        print(f'           mode_stack[-1] : {mode_stack[-1]}')
        mode_stack[-1].finish()
        mode_stack.pop

    mode_stack.append(mode)
    mode.init_mode()

    #왜이러는거야진짜로


