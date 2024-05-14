from src.RandomNumberGenerator import random_number_generator 
from typing import TextIO, List, Dict
from .helper.Splitter import splitter
from .helper.ListManipulation import table_print, to_list, join
from .helper.Readline import readlines
from .helper.IsType import is_number
import sys, time

# type Vector = List[List[str]]

def delay_print(s, t=0):
    for i in s:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(t)
    print("")
      
def battle(x: int):
    monster=random_number_generator(1,100,0)
    nama=random_number_generator(1,100,random_number_generator(1,100,0))
    print("*GAMBAR MONSTER*")
    print("")
    monster_data: TextIO = readlines('/Users/felix/Documents/Pengkom/GitHub/if1210-2024-tubes-k10-b/data/monster.csv')
    for i in range(monster+1):
            data = splitter(monster_data[i])
    delay_print(f"RAWRRR, Monster {data[1]} telah muncul !!! \n")
    lvl_m=random_number_generator(1,4,1)
    power_m = int (float (data[2]) *(1+(lvl_m-1)*1/10))
    def_m = int (float (data[3]) *(1+(lvl_m-1)*1/10))
    hp_m = int (float (data[4]) *(1+(lvl_m-1)*1/10))
    delay_print (f"Name       : {data[1]}")
    delay_print (f"ATK Power  : {power_m}")
    delay_print (f"DEF Power  : {def_m}")
    delay_print (f"HP         : {hp_m}")
    delay_print (f"Level      : {lvl_m}\n")
    # if (x<=1):
        #pilih Monster
        #print("============ MONSTER LIST ============\n")
    # else:
    #     # monster sudah di set
        

    hp_p=2000
    hp_ori=2000
    power_p=400
    def_p=25
    lvl_p=1
    match=True
    turn=1
    player="pika"
    pernah1=0
    pernah2=0
    pernah3=0
    while(match):
        if (turn%2==0):
            #Gambar monster
            print(f"============ TURN {turn} ({data[1]})============\n")
            hp_p= hp_p-(power_m)
            if (hp_p<0):
                hp_p=0
            print ("GAMBAR MONSTER \n")
            delay_print(f"SCHWINKKK, {data[1]} menyerang {player}\n")
            delay_print (f"Name       : {player}")
            delay_print (f"ATK Power  : {power_p}")
            delay_print (f"DEF Power  : {def_p}")
            delay_print (f"HP         : {hp_p}")
            delay_print (f"Level      : {lvl_p}\n")
            turn+=1
            if (hp_p==0):
                if (x>=1):
                        return False
                else:
                    delay_print (f"Yahhh, Anda dikalahkan monster {data[1]}. Jangan menyerah, coba lagi !!!")
                match=False
            time.sleep(0.2)
        else:
            print(f"============ TURN {turn} ({player})============")
            delay_print("1. Attack")
            delay_print("2. Use Potion")
            delay_print("3. Quit")
            pilihan=int(input("Pilhan Perintah: "))
            print ("")
            if (pilihan==3):
                delay_print("Anda berhasil kabur dari BATTLE!")
                match=False
            elif(pilihan == 1):
                print("GAMBAR MONSTER \n")
                delay_print(f"SCHWINKKK, {player} menyerang {data[1]} \n")
                hp_m= hp_m-(power_p)
                if (hp_m<0):
                    hp_m=0
                delay_print (f"Name       : {data[1]}")
                delay_print (f"ATK Power  : {power_m}")
                delay_print (f"DEF Power  : {def_m}")
                delay_print (f"HP         : {hp_m}")
                delay_print (f"Level      : {lvl_m}\n")
                if (hp_m==0):
                    if (x>=1):
                        return True
                    else:
                        delay_print (f"Selamat, Anda berhasil mengalahkan monster {data[1]} !!! \n")
                        OC=random_number_generator(5,30)
                        delay_print (f"Total OC yang diperoleh: {OC}")
                        #update nilai OC player
                    match=False
                turn+=1
            elif (pilihan == 2):
                jlh_potion=3
                if (jlh_potion==0):
                    delay_print ("Anda tidak memiliki Potion dalam inventory!")
                else:
                    potion=True
                    while (potion):
                        print ("============ POTION LIST ============")
                        delay_print (f"1. Strength Potion (Qty: JUMLAH) - Increases ATK Power")
                        delay_print (f"2. Resilience Potion (Qty: JUMLAH) - Increases DEF Power")
                        delay_print (f"3. Healing Potion (Qty: JUMLAH) - Restores Health")
                        delay_print ("4. Cancel")
                        pilihan_p = int(input("Pilihan Potion: "))
                        print("")
                        if (pilihan_p == 1) :
                            if (pernah1==1):
                                delay_print(f"Kamu mencoba memberikan ramuan ini kepada {player}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi. \n")
                            else:
                                power_p=potion(1,power_p)#fungsi potion
                                delay_print(f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {player} dan gerakannya menjadi lebih cepat dan mematikan. \n")
                                pernah1=1
                                delay_print (f"Name       : {player}")
                                delay_print (f"ATK Power  : {power_p}")
                                delay_print (f"DEF Power  : {def_p}")
                                delay_print (f"HP         : {hp_p}")
                                delay_print (f"Level      : {lvl_p}\n")
                                potion=False
                                turn+=1
                        elif (pilihan_p == 2) :
                            if (pernah2==1):
                                delay_print(f"Kamu mencoba memberikan ramuan ini kepada {player}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi. \n")
                            else:
                                delay_print(f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {player} yang membuatnya terlihat semakin tangguh dan sulit dilukai \n")
                                def_p=potion(2,def_p)#fungsi
                                pernah2=1
                                delay_print (f"Name       : {player}")
                                delay_print (f"ATK Power  : {power_p}")
                                delay_print (f"DEF Power  : {def_p}")
                                delay_print (f"HP         : {hp_p}")
                                delay_print (f"Level      : {lvl_p}\n")
                                potion=False
                                turn+=1
                        elif (pilihan_p == 3) :
                            if (pernah3==1):
                                delay_print(f"Kamu mencoba memberikan ramuan ini kepada {player}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            else:
                                delay_print (f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {player} sembuh dengan cepat. Dalam sekejap, {player} terlihat kembali prima dan siap melanjutkan pertempuran. \n")
                                hp_p=hp_p+potion(3,hp_ori)
                                pernah3=1
                                if (hp_p>hp_ori):
                                    hp_p=hp_ori 
                                delay_print (f"Name       : {player}")
                                delay_print (f"ATK Power  : {power_p}")
                                delay_print (f"DEF Power  : {def_p}")
                                delay_print (f"HP         : {hp_p}")
                                delay_print (f"Level      : {lvl_p}\n")
                                potion=False     
                                turn+=1
                        elif (pilihan_p==4):
                            potion=False        
                #turn+=1
            time.sleep(0.2)