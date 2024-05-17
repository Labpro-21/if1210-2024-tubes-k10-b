from typing import TextIO, List, Dict
Matrix = List[List[str]]
Mapping = Dict[str, Matrix]
import sys,time

def delay_print(s, t=0.015):
    for i in s:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(t)
    print("")

def arena (data:List[str], user_data: Mapping, x:int , n:int, dmg_taken:int ,dmg_given:int,monster:str,power:int,defend:int,hp:int,lvl_p,monster_p:int):
    # x = 1 menunjukkan player belum kalah
    # x = 0 menunjukkan player sudah kalah
    # x = 2 menunjukkan player mengakhiri arena
    # n menunjuukan stage
    reward = int(0)
    if (n>1):
        if (n==2):
            reward= 30
        elif (n==3):
            reward = 50
        elif (n==4):
            reward = 100
        elif (n==5):
            reward = 150
        elif (n==6):
            reward = 200
        if(x==1):
            delay_print (f"STAGE CLEARED! Anda akan mendapatkan {reward} OC pada sesi ini !\n")
    from src.Battle import battle
    if (x==1) and (n<=5):
        battle(data,user_data,n,monster,power,defend,hp,dmg_given,dmg_taken,lvl_p,monster_p)
    else:
        if (x==2):
            delay_print ("GAME OVER! Anda mengakhiri sesi latihan!\n")
        else:
            if (n<6):
                delay_print(f"GAME OVER! Sesi latihan berakhir pada stage {n-1}\n")
            else:
                delay_print (f"Selamat! Anda berhasil menyelesaikan seluruh stage Arena !!!\n")
        delay_print ("============ STATS ============")
        delay_print (f"Total hadiah    : {reward} OC")
        delay_print (f"Jumlah stage    : {n-1}")
        delay_print (f"Damage diberikan: {dmg_given}")
        delay_print (f"Damage diterima : {dmg_taken}")
        data[4]=str(int(data[4])+reward)
    # return


