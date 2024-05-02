from typing import TextIO, List
from .helper.Splitter import splitter
from .helper.ListManipulation import table_print, to_list
from .helper.Readline import readlines
from .helper.IsType import is_number


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


def show(c: str) -> None:
    if c == 'monster':
        monster_shop: TextIO = readlines('./data/monster_shop.csv')
        monster: TextIO = readlines('./data/monster.csv')
        monster_to_print: List[str] = concat(monster, monster_shop)
        table_print(monster_to_print)
    elif c == 'potion':
        item_shop: TextIO = readlines('./data/item_shop.csv')
        table_print(to_list(item_shop))


def lihat():
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c)
        if c in ['monster', 'potion']:
            breaked: bool = True


def is_in(arr: List[str], e: str, idx: int) -> bool:
    for i in arr:
        if i[idx] == e:
            return True
    return False


def tambah() -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        if c in ['monster', 'potion']:
            breaked = True
    for i in ['Healing Potion']:
        if not is_in(monster, i, 1):
            return
    return


def ubah() -> None:
    return


def write_without(path: str, idx: str) -> None:
    data: List[str] = readlines(path)
    data_2d: List[List[str]] = to_list(data)
    data_to_write: TextIO = open(path, 'w')
    txt_to_write: str = ""
    for i in range(len(data)):
        if data_2d[i][0] != idx:
            txt_to_write += data[i]
    data_to_write.write(txt_to_write)
    data_to_write.close()


def hapus() -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c)
        if c in ['monster', 'potion']:
            breaked = True
    monster_shop: TextIO = readlines('./data/monster_shop.csv')
    monster: TextIO = readlines('./data/monster.csv')
    monster_list: List[List[str]] = concat(monster, monster_shop)
    idx: str = input(">>> Masukkan id monster: ")
    while not (is_number(idx) and is_in(monster_list, idx, 0)):
        if not is_number(idx):
            print("Masukkan input bertipe Integer, coba lagi!")
        else:
            print("ID tidak ada dalam data!")
        print()
        idx = input(">>> Masukkan id monster: ")
    is_hapus: str = ""
    while is_hapus.lower() not in ['y', 'n']:
        is_hapus: str = input(
            ">>> Apakah anda yakin ingin menghapus Strength Potion dari shop (y/n)? ")
        if is_hapus.lower() == 'y':
            write_without('./data/monster.csv', idx)
            write_without('./data/monster_shop.csv', idx)
    return


def shop_management() -> None:
    print("Irasshaimase! Selamat datang kembali, Mr. Admin!\n")
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
            print("Dadah Mr. Admin")
            breaked: bool = True

    return
