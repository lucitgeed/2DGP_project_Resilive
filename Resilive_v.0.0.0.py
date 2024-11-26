from pico2d import*
import mode_play as start_mode

import game_world
import handle_framework
from mode_play import handle_events


##
open_canvas()

handle_framework.run(start_mode)


close_canvas()
#1. lilly의 x와 y 서로 영향안가게 분리하는 방법은?(점프)



#2. 어그로랑 어택을 구분하는 방법은??
#3. community 몬스터의 경우, 상태 변환을 하면 (statemachine으로 보내면)lilly의 상태로 입력이 되는데 , 새로운 statemachine을 만들지않고 어떻게 해결해야?
#