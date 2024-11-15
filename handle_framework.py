

def run(start_mode):
    global running
    running = True

    global mode_stack
    mode_stack = [start_mode]
    start_mode.init_mode()

    while(running):
        mode_stack[-1].handle_events()
        mode_stack[-1].update()
        mode_stack[-1].draw()

    while(len(mode_stack) > 0):
        mode_stack[-1].finish()
        mode_stack.pop()
    pass