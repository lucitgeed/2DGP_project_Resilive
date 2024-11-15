

running = None
mode_stack = None



def run(mode):
    global running
    running = True

    global mode_stack
    mode_stack = [mode]
    mode.init_mode()

    while(running):
        mode_stack[-1].handle_events()
        mode_stack[-1].update()
        mode_stack[-1].draw()

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



def quit():
    global running
    running = False
    pass
