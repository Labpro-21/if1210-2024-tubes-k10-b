from .helper.ListManipulation import to_list, readlines
from .helper.IsType import is_number
from typing import List, Tuple, Dict

type Matrix = List[List[str]]
type Mapping = Dict[str, Matrix]

def get_item_data(idn: str, user_data: str) -> Matrix:
    arr = []
    for i in user_data:
        if i[0] == idn:
            arr.append(i)
    return arr


def get_monster_data(idn: str, user_data: Matrix) -> Matrix:
    arr = []
    for i in user_data:
        if i[0] == idn:
            arr.append(i)
    return arr


def concat_monster(a1: Matrix, a2: Matrix) -> None:
    for i in range(len(a1)):
        for j in a2:
            if a1[i][1] == j[0]:
                for k in range(1, 5):
                    a1[i].append(j[k])


def concat_monster_item(a1: Matrix, a2: Matrix) -> List[Tuple[str, List[str]]]:
    arr = []
    for i in a1:
        arr.append(('monster', i))
    for i in a2:
        arr.append(('potion', i))
    return arr


def inventory(data: List[str], user_data: Mapping) -> None:
    print("============ INVENTORY LIST (User ID: %s) ============" % (data[0]))
    print("Jumlah O.W.C.A. Coin-mu sekarang %s." % (data[4]))
    monster_inv: Matrix = get_monster_data(data[0], user_data["monster_inventory.csv"])
    monster: Matrix = user_data["monster.csv"]
    concat_monster(monster_inv, monster)
    item_inv: Matrix = get_item_data(data[0], user_data["item_inventory.csv"])
    num: int = 1
    all_data: Matrix = concat_monster_item(monster_inv, item_inv)
    for inv in monster_inv:
        print("%s. Monster\t(Name: %s, Lvl: %s, HP: %s)" %
              (num, inv[3], inv[2], inv[6]))
        num += 1

    kamus_potion = {
        "strength": "ATK",
        "healing": "Heal",
        "resilience": "DEF"
    }
    for inv in item_inv:
        print("%s. Potion\t(Type: %s, Qty: %s)" %
              (num, kamus_potion[inv[1]], inv[2]))
        num += 1

    c = ""
    while c != "KELUAR":
        print("\nKetikkan id untuk menampilkan detail item:")
        c = input(">>> ")
        if c != "KELUAR" and is_number(c):
            if 1 <= int(c) <= len(all_data):
                c = int(c)-1
                if all_data[c][0] == 'monster':
                    print("Monster")
                    print("Name\t  : %s" % (all_data[c][1][3]))
                    print("ATK Power : %s" % (all_data[c][1][4]))
                    print("DEF Power : %s" % (all_data[c][1][5]))
                    print("HP\t  : %s" % (all_data[c][1][6]))
                    print("Level\t  : %s" % (all_data[c][1][2]))
                elif all_data[c][0] == 'potion':
                    print("Potion")
                    print("Type      : %s" % (kamus_potion[all_data[c][1][1]]))
                    print("Quantity  : %s" % (all_data[c][1][2]))
            else:
                print("Indeks yang dimasukkan tidak ada!")

        elif c != 'KELUAR':
            print("Masukkan bilangan integer positif!")
