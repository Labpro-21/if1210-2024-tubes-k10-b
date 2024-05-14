from typing import List, Dict
from .helper.IsType import is_number
from src.ShopManagement import is_in
 
Matrix = List[List[str]]
Mapping = Dict[str, Matrix]
 
 
def get_name_by_id(idx: str, data) -> str:
    for i in data:
        if i[0] == idx:
            return i[1]
    return None
 
 
def get_id(n: int) -> int:
    c: str = input(">>> Pilih monster: ")
    while not is_number(c) or not (1 <= int(c) <= n):
        if not (1 <= int(c) <= n):
            print("Urutan tidak ditemukan!")
        c: str = input(">>> Pilih monster: ")
    return int(c)
 
 
def verif() -> bool:
    while True:
        c: str = input(">>> Lanjutkan upgrade (Y/N): ")
        if c.lower() == 'y':
            return True
        elif c.lower() == 'n':
            return False
 
 
def laboratory(user_login: List[str], user_data: Mapping):
    print("Selamat datang di Lab Dokter Asep  !!!\n")
    print("============ MONSTER LIST ============")
    monster_list: Matrix = []
    for row in user_data["monster_inventory.csv"]:
        if row[0] == user_login[0]:
            monster_list.append(row)
    for i, row in enumerate(monster_list, 1):
        print("%s. %s (Level: %s)" % (i, get_name_by_id(
            row[1], user_data["monster.csv"]), row[2]))
    print()
    print("============ UPGRADE PRICE ============")
    print("1. Level 1 -> Level 2: 300 OC")
    print("2. Level 2 -> Level 3: 500 OC")
    print("3. Level 3 -> Level 4: 800 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
 
    harga = {
        "2": 300,
        "3": 500,
        "4": 800,
        "5": 1000
    }
    idx: int = get_id(len(monster_list))
    if monster_list[idx-1][2] == '5':
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
    else:
        monster_name: str = get_name_by_id(
            monster_list[idx-1][1], user_data["monster.csv"])
        lvl: int = int(monster_list[idx-1][2]) + 1
        print("\n%s akan di-upgrade ke level %d." %
              (monster_name, lvl))
        print("Harga untuk melakukan upgrade %s adalah %s OC." %
              (monster_name, harga[str(lvl)]))
        if verif():
            print()
            if int(user_login[4]) < harga[str(lvl)]:
                print("OC tidak cukup")
            else:
                monster_list[idx-1][2] = str(lvl)
                user_login[4] = str(int(user_login[4]) - harga[str(lvl)])
                print("Selamat, %s berhasil di-upgrade ke level %s !" % (monster_name, lvl))