from src.RandomNumberGenerator import random_number_generator
import time,sys
def stats_Monster(lvl:int,y:int):
    x=int (float (y) *(1+(lvl-1)*1/10))
    return x

def def_monster_a(defend,att_enemy):
    x= random_number_generator(1,defend+1)
    x-=1
    y= int(float(att_enemy*(100-x)/100))
    return y


def attack_monster_a(power):
    x = int(float(power*70/100))
    y = int(float(power*130/100))
    return random_number_generator(x,y)

def def_monster_b(defend,att_enemy):
    x= random_number_generator(1,defend,int(time.time())+def_monster_a(defend,att_enemy)+1)
    x-=1
    y= int(float(att_enemy*(100-x)/100))
    return y


def attack_monster_b(power):
    x = int(float(power*70/100))
    y = int(float(power*130/100))
    return random_number_generator(x,y,int(time.time())+attack_monster_a(power))

def def_monster_c(defend,att_enemy):
    x= random_number_generator(1,defend,int(time.time())+def_monster_b(defend,att_enemy)+1)
    x-=1
    y= int(float(att_enemy*(100-x)/100))
    return y


def attack_monster_c(power):
    x = int(float(power*70/100))
    y = int(float(power*130/100))
    return random_number_generator(x,y,int(time.time())+attack_monster_b(power))