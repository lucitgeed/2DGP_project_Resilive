from pico2d import*
import mode_title as start_mode

import game_world
import handle_framework
from mode_play import handle_events


##
open_canvas()

handle_framework.run(start_mode)


close_canvas()
