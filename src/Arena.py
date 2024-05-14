def arena (x=1/0,n=stage,dmg_taken,dmg_given):
    alive=True
    n=int(0)
    reward = int(0)
    dmg_taken=int(0)
    dmg_given=int(0)
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
        print (f"STAGE CLEARED! Anda akan mendapatkan {reward} OC pada sesi ini !")
    if (x==1) and (n<=5):
        n+=1
        battle(n)
    else:
        if (x==2):
            print ("GAME OVER! Anda mengakhiri sesi latihan!")
        if (n<=6):
            print(f"GAME OVER! Sesi latihan berakhir pada stage {n-1} ")
        else:
            print (f"Selamat! Anda berhasil menyelesaikan seluruh stage Arena !!!")
        print ("============ STATS ============")
        print (f"Total hadiah    :{reward}")
        print (f"Jumlah stage    : {n-1}")
        print (f"Damage diberikan: {dmg_given}")
        print (f"Damage diterima : {dmg_taken}")

