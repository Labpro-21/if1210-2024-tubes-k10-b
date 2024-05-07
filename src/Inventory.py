from .helper.ListManipulation import to_list
from .helper.Readline import readlines
from .helper.IsType import is_number
from typing import List, Tuple


def get_item_data(idn: str, folder_name: str) -> List[List[str]]:
    item: List[List[str]] = to_list(readlines('./data/%s/item_inventory.csv' % (folder_name)))
    arr = []
    for i in item:
        if i[0] == idn:
            arr.append(i)
    return arr


def get_monster_data(idn: str, folder_name: str) -> List[List[str]]:
    monster: List[List[str]] = to_list(
        readlines('./data/%s/monster_inventory.csv' % (folder_name)))
    arr = []
    for i in monster:
        if i[0] == idn:
            arr.append(i)
    return arr


def concat_monster(a1: List[List[str]], a2: List[List[str]]) -> None:
    for i in range(len(a1)):
        for j in a2:
            if a1[i][1] == j[0]:
                for k in range(1, 5):
                    a1[i].append(j[k])


def concat_monster_item(a1: List[List[str]], a2: List[List[str]]) -> List[Tuple[str, List[str]]]:
    arr = []
    for i in a1:
        arr.append(('monster', i))
    for i in a2:
        arr.append(('potion', i))
    return arr


def inventory(data: List[str], folder_name: str) -> None:
    print("============ INVENTORY LIST (User ID: %s) ============" % (data[0]))
    print("Jumlah O.W.C.A. Coin-mu sekarang %s." % (data[4]))
    monster_inv: List[List[str]] = get_monster_data(data[0], folder_name)
    monster: List[List[str]] = to_list(readlines('./data/%s/monster.csv' % (folder_name)))
    concat_monster(monster_inv, monster)
    item_inv: List[List[str]] = get_item_data(data[0], folder_name)
    num: int = 1
    all_data: List[List[str]] = concat_monster_item(monster_inv, item_inv)
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
