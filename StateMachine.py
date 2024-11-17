from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_d, SDL_KEYUP, SDLK_a, SDLK_UP, SDLK_LSHIFT

from dataclasses import asdict
from multiprocessing.connection import answer_challenge
from xml.dom.minicompat import defproperty



class StateMachine:
    def __init__(self, objt):
        self.objt = objt
        self.event_que = []

    def start(self, start_state):
        self.cur_state = start_state

        #더미?
        self.cur_state.enter(self.objt, ('Start', 0))
        #더미?

        print(f'Enter into {self.cur_state}')
        pass

    def update(self):
        self.cur_state.do(self.objt)
      #  print(f'    Now in {self.cur_state}')

        if self.event_que:
            e = self.event_que.pop(0)

            for check_event, next_event in self.transitions[self.cur_state].items():
                if check_event(e):
                    self.cur_state.exit(self.objt, e)
                    print(f'Exit from {self.cur_state}')
                    self.cur_state = next_event
                    self.cur_state.enter(self.objt,e)
                    print(f'Enter into {self.cur_state}')
                    return

    def draw(self):
        self.cur_state.draw(self.objt)
        pass

    def set_transitions(self, transitions):
        self.transitions = transitions
        pass

    def add_events(self, e):
        self.event_que.append(e)
        print(f'                [DEBUG]: New event {e} is appended')
        pass



##################
def start_event(e):
    return e[0] == 'Start'
def time_out(e):
    return e[0] == 'Time_Out'


#def for Walk
def right_down(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d)
def right_up(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d)

def left_down(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a)
def left_up(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a)


#def for Run
def shift_down(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LSHIFT)
def shift_up(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LSHIFT)


#def for Jump
def space_down(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE)
def space_up(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE)

def landed(e):
    return e[0] == 'Landed'         #충돌체크하면 land

#def for Crawl
def ctrl_down(e):
    return (e[0] == 'Input' and e[1].type == SDL_KEYDOWN)
