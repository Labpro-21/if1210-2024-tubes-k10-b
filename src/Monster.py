def stats_Monster(lvl,y=int):
    x=int (float (y) *(1+(lvl-1)*1/10))
    return x

def def_monster(defend,att_enemy):
    x= random_number_generator(0,defend)
    y= int(float(att_enemy*(100-x)/100))
    return y


def attack_monster(power):
    x = int(float(power*70/100))
    y = int(float(power*130/100))
    return random_number_generator(x,y)

