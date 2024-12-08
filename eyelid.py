import random

from pico2d import load_image, draw_rectangle

import handle_framework
from StateMachine import StateMachine

#set eyelid frame flip speed
TIME_per_BLINK_ACTION = 2.5
BLINK_ACTION_per_TIME = 1.0 / TIME_per_BLINK_ACTION


