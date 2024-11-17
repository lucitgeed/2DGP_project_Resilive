world = [ [] for _ in range(4)]
collision_pairs = {}


def add_object(objt, depth):
    world[depth].append(objt)
    pass
def add_objts(objt, depth):
    world[depth] += objt
    pass
#----------------------------------------
def add_collision_info(crashedgroup,a ,b):
    if crashedgroup not in collision_pairs:             #crashedgroup라는 key가 없다면,
        collision_pairs[crashedgroup] = [[], []]        #리스트를 초기화!
    if a:
        collision_pairs[crashedgroup][0].append(a)
    if b:
        collision_pairs[crashedgroup][1].append(b)
    pass


################
def update():
     for layer in world:
        for objt in layer:
             objt.update()

def render():
    for layer in world:
        for objt in layer:
            objt.draw()
#--------------------
def collided(a,b):
    aleft, abottom, aright, atop =
    pass

def handle_collisions():
    pass



######################
def remove_objt(objt):
    for layer in world:
        if objt in layer:
            world.remove(objt)
            return
#------------------------------
def remove_collision_objt(objt):
    for pairs in collision_pairs.values():
        if objt in pairs[0]:
            pairs[0].remove(objt)
        if objt in pairs[1]:
            pairs[1].remove(objt)
    pass


###############
def clear():
    for layer in world:
        layer.clear()
    pass