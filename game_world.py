world = [ [] for _ in range(4)]


def add_object(objt, depth):
    world[depth].append(objt)
    pass
def add_objts(objt, depth):
    world[depth] += objt
    pass


def update():
     for layer in world:
        for objt in layer:
             objt.update()

def render():
    for layer in world:
        for objt in layer:
            objt.draw()


def remove_objt(objt):
    for layer in world:
        if objt in layer:
            world.remove(objt)
            return


def clear():
    for layer in world:
        layer.clear()
    pass