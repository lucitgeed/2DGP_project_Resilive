class State_Machine:
    def __init__(self, objt):
        self.objt = objt
        pass

    def start(self, start_state):
        self.cur_state = start_state
        print(f'Enter into {self.cur_state}')
        pass

    def update(self):
        self.cur_state.do(self.objt)
        pass

    def draw(self):
        pass
