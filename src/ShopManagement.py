from typing import TextIO, List
from .helper.Splitter import splitter
from .helper.ListManipulation import table_print, to_list
from .helper.Readline import readlines


def concat(a1: List[str], a2: List[str]) -> List[List[str]]:
    a1: List[List[str]] = to_list(a1)
    a2: List[List[str]] = to_list(a2)
    row: int = len(a1)
    col_a1: int = len(a1[0])
    col_a2: int = len(a2[0])
    col: int = col_a1 + col_a2 - 1
    new_arr: List[str] = [["" for _ in range(col)] for _ in range(row)]
    for i in range(1):
        for j in range(col_a1):
            new_arr[i][j] = a1[i][j]
        for j in range(1, col_a2):
            new_arr[i][col_a1+j-1] = a2[i][j]

    for i in range(1, row):
        for j in range(col_a1):
            new_arr[i][j] = a1[i][j]
        idx: str = -1
        for j in range(len(a2)):
            if new_arr[i][0] == a2[j][0]:
                idx = j
        if idx != -1:
            for j in range(1, col_a2):
                new_arr[i][col_a1+j-1] = a2[idx][j]
    return new_arr


def lihat():
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        if c == 'monster':
            monster_shop: TextIO = readlines('./data/monster_shop.csv')
            monster: TextIO = readlines('./data/monster.csv')
            monster_to_print: List[str] = concat(monster, monster_shop)
            table_print(monster_to_print)
            breaked: bool = True
        elif c == 'potion':
            item_shop: TextIO = readlines('./data/item_shop.csv')
            table_print(to_list(item_shop))
            breaked: bool = True

def tambah() -> None:
    return

def ubah() -> None:
    return

def hapus() -> None:
    return

def shop_management() -> None:
    print("Irasshaimase! Selamat datang kembali, Mr. Monogram!\n")
    breaked: bool = False
    while not breaked:
        act: str = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
        if act.lower() == 'lihat':
            lihat()
            breaked: bool = True
        elif act.lower() == 'tambah':
            tambah()
            breaked: bool = True
        elif act.lower() == 'ubah':
            ubah()
            breaked: bool = True
        elif act.lower() == 'hapus':
            hapus()
            breaked: bool = True
        elif act.lower() == 'keluar':
            breaked: bool = True

    return
