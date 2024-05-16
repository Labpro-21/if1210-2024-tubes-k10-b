from src.RandomNumberGenerator import random_number_generator 
from src.Arena import arena
from src.Monster import stats_Monster,attack_monster_b,def_monster_b,attack_monster_c,def_monster_c
from src.Potion import potion
from src.AsciiArt import ascii_battle
from typing import TextIO, List, Dict
import sys, time
Matrix = List[List[str]]
Mapping = Dict[str, Matrix]

def delay_print(s, t=0.015):
    for i in s:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(t)
    print("")
      
def battle(data: List[str], user_data: Mapping ,n: int,player,power_p,def_p,hp_p,dmg_given,dmg_taken,lvl_p):
    jlh_monster=len(user_data["monster.csv"])
    monster=random_number_generator(1,jlh_monster-1,int(time.time())+random_number_generator(1,100))
    ascii_battle(monster)
    print("")
    delay_print(f"RAWRRR, Monster {user_data['monster.csv'][monster][1]} telah muncul !!! \n")
    lvl_m=random_number_generator(1,4,int(time.time())+random_number_generator(1,100))
    nama_m= user_data['monster.csv'][monster][1]
    power_m = stats_Monster(lvl_m,int(user_data['monster.csv'][monster][2]))
    def_m = stats_Monster(lvl_m,int(user_data['monster.csv'][monster][3]))
    hp_m = stats_Monster(lvl_m,int(user_data['monster.csv'][monster][4]))
    delay_print (f"Name       : {nama_m}")
    delay_print (f"ATK Power  : {power_m}")
    delay_print (f"DEF Power  : {def_m}")
    delay_print (f"HP         : {hp_m}")
    delay_print (f"Level      : {lvl_m}\n")

    if (n<=1):
        delay_print("============ MONSTER LIST ============\n")
        j=int(1)
        list_lvl=[0 for i in range (1)]
        list_power=[0 for i in range (1)]
        list_def=[0 for i in range (1)]
        list_hp=[0 for i in range (1)]
        list_nama=[''for i in range (1)]
        for i in range (0,len(user_data["monster_inventory.csv"])):
            if (user_data["monster_inventory.csv"][i][0]==data[0]):
                indeks=int(user_data["monster_inventory.csv"][i][1])+1
                delay_print(f"{j}. {user_data['monster.csv'][indeks][1]}")
                j+=1
                list_lvl.append(int(user_data["monster_inventory.csv"][i][2]))
                list_power.append(int(user_data["monster.csv"][indeks][2]))
                list_def.append(int(user_data["monster.csv"][indeks][3]))
                list_hp.append(int(user_data["monster.csv"][indeks][4]))
                list_nama.append(user_data['monster.csv'][indeks][1])

        pilih=True
        while (pilih):
            delay_print("Pilih monster untuk bertarung: ")
            monster_p=int(input(""))
            if (monster_p>j-1):
                delay_print("Pilihan nomor tidak tersedia!\n")
            else:
                pilih=False
                ascii_battle(monster_p)
                lvl_p=list_lvl[monster_p]
                power_p=stats_Monster(lvl_p,list_power[monster_p])
                def_p=stats_Monster(lvl_p,list_def[monster_p])
                hp_ori=stats_Monster(lvl_p,list_hp[monster_p])
                hp_p=hp_ori
                player=list_nama[monster_p]
    else:
        hp_ori=hp_p
        print(f"\n============ STAGE {n} ============\n")
    match=True
    turn=1
    pernah1=0
    pernah2=0
    pernah3=0
    while(match):
        if (turn%2==0):
            ascii_battle(monster)
            delay_print(f"============ TURN {turn} ({nama_m})============\n")
            att=attack_monster_c(power_m)
            serangan=def_monster_c(def_p,att)
            hp_p-=serangan
            dmg_taken+=serangan
            if (hp_p<0):
                dmg_taken+=hp_p
                hp_p=0
            print ("GAMBAR MONSTER \n")
            delay_print (f"SCHWINKKK, {nama_m} menyerang {player}\n")
            delay_print ("DETAIL SERANGAN:")
            delay_print (f"{nama_m} mencoba untuk menyerang {player} dengan power sebesar {att} ({int(float((att-power_m)/power_m*100))}%)")
            delay_print (f"{player} menahan serangan dari {nama_m} sebesar {att-serangan} ({int(float((att-serangan)/att*100))}%)")
            delay_print (f"sehingga damage yang diterima oleh {player} sebesar {serangan}\n")

            delay_print (f"Name       : {player}")
            delay_print (f"ATK Power  : {power_p}")
            delay_print (f"DEF Power  : {def_p}")
            delay_print (f"HP         : {hp_p}")
            delay_print (f"Level      : {lvl_p}\n")

            turn+=1
            if (hp_p==0):
                if (n>=1):
                    arena(data,user_data,0,n,dmg_taken,dmg_given,player,power_p,def_p,hp_ori,lvl_p)
                else:
                    delay_print (f"Yahhh, Anda dikalahkan monster {nama_m}. Jangan menyerah, coba lagi !!!")
                match=False
            time.sleep(0.2)
        else:
            print(f"============ TURN {turn} ({player})============")
            delay_print("1. Attack")
            delay_print("2. Use Potion")
            delay_print("3. Quit")
            pilihan=int(input("Pilhan Perintah: "))
            time.sleep(1)
            print ("")
            if (pilihan==3):
                if (n>=1):
                    arena(data,user_data,2,n,dmg_taken,dmg_given,player,power_p,def_p,hp_ori,lvl_p)
                else:
                    delay_print("Anda berhasil kabur dari BATTLE!")
                match=False
            elif(pilihan == 1):
                ascii_battle(monster_p)
                delay_print(f"SCHWINKKK, {player} menyerang {nama_m} \n")
                att=attack_monster_b(power_p)
                serangan=def_monster_b(def_m,att)
                hp_m-=serangan
                dmg_given+=serangan
                delay_print ("DETAIL SERANGAN:")
                delay_print (f"{player} mencoba untuk menyerang {nama_m} dengan power sebesar {att} ({int(float((att-power_p)/power_p*100))}%)")
                delay_print (f"{nama_m} menahan serangan dari {player} sebesar {att-serangan} ({int(float((att-serangan)/att*100))}%)")
                delay_print (f"sehingga damage yang diterima oleh {nama_m} sebesar {serangan}\n")
                if (hp_m<0):
                    dmg_given+=hp_m
                    hp_m=0
                delay_print (f"Name       : {nama_m}")
                delay_print (f"ATK Power  : {power_m}")
                delay_print (f"DEF Power  : {def_m}")
                delay_print (f"HP         : {hp_m}")
                delay_print (f"Level      : {lvl_m}\n")
                if (hp_m==0):
                    if (n>=1):
                        n+=1
                        arena(data,user_data,1,n,dmg_taken,dmg_given,player,power_p,def_p,hp_ori,lvl_p)
                    else:
                        delay_print (f"Selamat, Anda berhasil mengalahkan monster {nama_m} !!! \n")
                        oc=random_number_generator(5,30)
                        delay_print (f"Total OC yang diperoleh: {oc}")
                        data[4]=str(int(data[4])+oc)
                    match=False
                turn+=1
            elif (pilihan == 2):
                ada_potion=False
                list_potion=[0 for i in range (4)]
                letak_potion=[0 for i in range (4)]
                for i in range (1,len(user_data["item_inventory.csv"])):
                    if (user_data["item_inventory.csv"][i][0]==data[0]):
                        if (user_data["item_inventory.csv"][i][1]=="strength"):
                            list_potion[1]=int(user_data["item_inventory.csv"][i][2])
                            letak_potion[1]=i
                        elif (user_data["item_inventory.csv"][i][1]=="resilience"):
                            list_potion[2]=int(user_data["item_inventory.csv"][i][2])
                            letak_potion[2]=i
                        elif (user_data["item_inventory.csv"][i][1]=="healing"):
                            list_potion[3]=int(user_data["item_inventory.csv"][i][2])
                            letak_potion[3]=i
                        ada_potion=True
                if (ada_potion==False):
                    delay_print ("Anda tidak memiliki Potion dalam inventory!")
                else:
                    potions=True
                    while (potions):
                        print ("============ POTION LIST ============")
                        delay_print (f"1. Strength Potion (Qty: {list_potion[1]}) - Increases ATK Power")
                        delay_print (f"2. Resilience Potion (Qty: {list_potion[2]}) - Increases DEF Power")
                        delay_print (f"3. Healing Potion (Qty: {list_potion[3]}) - Restores Health")
                        delay_print ("4. Cancel")
                        pilihan_p = int(input("Pilihan Potion: "))
                        print("")
                        if (pilihan_p == 1) :
                            if (list_potion[1]==0):
                                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                            elif (pernah1==1):
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
                                user_data["item_inventory.csv"][letak_potion[1]][2]=int(user_data["item_inventory.csv"][letak_potion[1]][2])-1
                                potions=False
                                turn+=1
                        elif (pilihan_p == 2) :
                            if (list_potion[2]==0):
                                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                            elif (pernah2==1):
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
                                user_data["item_inventory.csv"][letak_potion[2]][2]=int(user_data["item_inventory.csv"][letak_potion[2]][2])-1
                                potions=False
                                turn+=1
                        elif (pilihan_p == 3) :
                            if (list_potion[3]==0):
                                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                            elif (pernah3==1):
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
                                user_data["item_inventory.csv"][letak_potion[3]][2]=int(user_data["item_inventory.csv"][letak_potion[3]][2])-1
                                turn+=1
                                potions=False
                        elif (pilihan_p==4):
                            potions=False
            time.sleep(0.2)