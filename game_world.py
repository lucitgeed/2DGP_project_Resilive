world = [] #아직아무것드 들어있지않는 리스트로 이뤄진 월드

def add_object(o):      #뭔진 모르지만 객체를 추가하는 함수
    world.append(o)
    pass



def update():
     for o in world:
         o.update()

def render():
    for o in world:
        o.draw()

#모든 객체를 다루는 모듈
# 모든 객체를 담는 리스트, 리스트에 추가하는 기능, 업데이트, 그리는 기능이 있어야함