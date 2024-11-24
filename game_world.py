world = [ [] for _ in range(7)]
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
def collided(a,b):                          #aggro & aggro
    aleft, abottom, aright, atop = a.get_boundingbox()
    
    bl, bb, br, bt = b.get_aggrobox()

    if br < aleft: return False
    if aright < bl: return False
    if bt < abottom: return False
    if atop < bb: return False

    return True
    pass

def collided_todeath(a,b):                  #bounding & bounding
    aleft, abottom, aright, atop = a.get_boundingbox()
    bl, bb, br, bt = b.get_boundingbox()

    if br < aleft: return False
    if aright < bl: return False
    if bt < abottom: return False
    if atop < bb: return False

    return True
    pass


#def collided_toattack(a,b):                 #bounding & aggro
#    aleft, abottom, aright, atop = a.get_boundingbox()
#    bl, bb, br, bt = b.get_aggrobox()

#    if br < aleft: return False
#    if aright < bl: return False
#    if bt < abottom: return False
#    if atop < bb: return False
#    return True


def handle_collisions():
    for crashgroup, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collided(a,b):

                    print(f'            {crashgroup} has collided')

                    a.handle_self_collision(crashgroup,b)
                    b.handle_self_collision(crashgroup,a)
    pass


def handle_death_collisions():
    for crashgroup, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collided_todeath(a,b):

                    print(f'            {crashgroup} has collided_to death')

                    a.handle_self_collision(crashgroup,b)
                    b.handle_self_collision(crashgroup,a)
    pass


#def handle_attack_collisions():
#    for crashgroup, pairs in collision_pairs.items():
#        for a in pairs[0]:
#            for b in pairs[1]:
#                if collided_toattack(a,b):

#                    print(f'            {crashgroup} has collided_to attack')

#                    a.handle_self_collision(crashgroup,b)
#                    b.handle_self_collision(crashgroup,a)


######################
def remove_objt(objt):
    for layer in world:
        if objt in layer:


#           자. 이러면 어떨까!?!
            layer.remove(objt)
#            world.remove(objt)

            return


#------------------------------
def remove_collision_objt(objt):
    for pairs in collision_pairs.values():
        if objt in pairs[0]:
            pairs[0].remove(objt)
        if objt in pairs[1]:
            pairs[1].remove(objt)
    pass


def remove_a_collision_objt(group, objt):
    if collision_pairs.keys() == group:
        collision_pairs.values()[0].remove(objt)
        pass


###############
def clear():
    for layer in world:
        layer.clear()
    pass