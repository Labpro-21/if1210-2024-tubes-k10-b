from typing import TextIO, List, Dict
from .helper.Splitter import splitter
from .helper.ListManipulation import table_print, to_list, join, readlines
from .helper.IsType import is_number

type Matrix = List[List[str]]
type Mapping = Dict[str, Matrix]


def lihat(folder_name):
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c, folder_name)
        if c in ['monster', 'potion']:
            breaked: bool = True


def tambah(user_data: Mapping) -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        if c in ['monster', 'potion']:
            breaked = True
    if c == 'monster':
        contoh: Matrix = [["ID", "Type", "ATK Power", "DEF Power", "HP"],
                          ["4", "Cici", "10", "1000", "200"],
                          ["5", "Moskov", "20", "1000", "200"],
                          ["6", "Selena", "30", "430", "100"]]
        monster = user_data["monster.csv"]
        arr = []
        for i in contoh:
            if is_in(monster, i[0], 0) == -1:
                arr.append(i)
        table_print(arr)
        idx: str = get_idx(arr, 'monster')
        stock: str = get_stock()
        price: str = get_price()
        idn: str = is_in(arr, idx, 0)
        user_data["monster.csv"].append(arr[idn])
        user_data["monster_shop.csv"].append([arr[idn][0], stock, price])
    elif c == 'potion':
        contoh: Matrix = [["ID", "Type"],
                          ["3", "Healing Potion"]]
        arr = []
        potion = user_data["item_shop.csv"]
        for i in contoh:
            if is_in(potion, i[0], 0) == -1:
                arr.append(i)
        table_print(arr)
        idx: str = get_idx(arr, 'potion')
        stock: str = get_stock()
        price: str = get_price()
        idn: int = is_in(arr, idx, 0)
        user_data["item_shop.csv"].append([arr[idn][1], stock, price])
    return


def ubah(user_data: Mapping) -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c, user_data)
        if c in ['monster', 'potion']:
            breaked = True
    if c == 'monster':
        monster_shop: List[str] = user_data["monster_shop.csv"]
        monster_list: Matrix = concat(
            user_data["monster.csv"], user_data["monster_shop.csv"])
        idx: str = get_idx(monster_list, 'monster')
        stock: str = get_stock()
        price: str = get_price()
        txt_to_write: str = ""
        for i in range(len(monster_shop)):
            row = monster_shop[i]
            if row[0] == idx:
                if stock != "":
                    row[1] = stock
                if price != "":
                    row[2] = price
                return
    elif c == 'potion':
        potion: Matrix = add_id(user_data["item_shop.csv"])
        idx: str = get_idx(potion, 'potion')
        stock: str = get_stock()
        price: str = get_price()
        potion: List[str] = user_data["item_shop.csv"]
        txt_to_write: str = ""
        for i in range(len(potion)):
            data = potion[i]
            if i == int(idx):
                if stock != "":
                    data[1] = stock
                if price != "":
                    data[2] = price
            return
    return


def hapus(user_data: Mapping) -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c, user_data)
        if c in ['monster', 'potion']:
            breaked = True
    if c == 'monster':
        monster_shop: Matrix = user_data["monster_shop.csv"]
        monster: Matrix = user_data["monster.csv"]
        monster_list: Matrix = concat(monster, monster_shop)
        idx: str = get_idx(monster_list, 'monster')
        if verification_hapus(idx, monster_list):
            user_data["monster_shop.csv"] = write_without(
                user_data["monster_shop.csv"], idx)
            user_data["monster.csv"] = write_without(
                user_data["monster.csv"], idx)
    elif c == 'potion':
        potion: Matrix = add_id(user_data["item_shop.csv"])
        idx: str = get_idx(potion, 'potion')
        if verification_hapus(idx, potion):
            user_data["item_shop.csv"] = write_without(
                user_data["item_shop.csv"], idx, True)
    return


def shop_management(user_data: Mapping) -> None:
    print("Irasshaimase! Selamat datang kembali, Mr. Admin!\n")
    breaked: bool = False
    while not breaked:
        act: str = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
        if act.lower() == 'lihat':
            lihat(user_data)
            breaked: bool = True
        elif act.lower() == 'tambah':
            tambah(user_data)
            breaked: bool = True
        elif act.lower() == 'ubah':
            ubah(user_data)
            breaked: bool = True
        elif act.lower() == 'hapus':
            hapus(user_data)
            breaked: bool = True
        elif act.lower() == 'keluar':
            print("Dadah Mr. Admin")
            breaked: bool = True
    return


def concat(a1: Matrix, a2: Matrix) -> Matrix:
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


def add_id(data: Matrix) -> Matrix:
    row: int = len(data)
    col: int = len(data[0])
    arr: Matrix = [["" for _ in range(col+1)] for _ in range(row)]
    for i in range(row):
        for j in range(col+1):
            if j == 0:
                if i == 0:
                    arr[i][j] = "ID"
                else:
                    arr[i][j] = str(i)
            else:
                arr[i][j] = data[i][j-1]
    return arr


def write_without(user_data: Matrix, idx: str, is_potion: bool = False) -> None:
    arr: Matrix = []
    if is_potion:
        for i in range(len(user_data)):
            if i != int(idx):
                arr.append(user_data[i])
    else:
        for i in range(len(user_data)):
            if user_data[i][0] != idx:
                arr.append(user_data[i])
    return arr


def verification_hapus(idx: str, user_data: Matrix) -> bool:
    is_hapus: str = ""
    while is_hapus.lower() not in ['y', 'n']:
        is_hapus: str = input(
            ">>> Apakah anda yakin ingin menghapus %s dari shop (y/n)? " % (user_data[is_in(user_data, idx, 0)][1]))
    if is_hapus.lower() == 'y':
        return True
    return False


def get_stock() -> str:
    stock: str = input(">>> Masukkan stok baru: ")
    while not (is_number(stock)) and len(stock) > 0:
        print("Masukkan input bertipe Integer nonnegatif, coba lagi!\n")
        stock = input(">>> Masukkan stok baru: ")
    return stock


def get_price() -> str:
    price: str = input(">>> Masukkan harga baru: ")
    while not (is_number(price)) and len(price) > 0:
        print("Masukkan input bertipe Integer nonnegatif, coba lagi!\n")
        price = input(">>> Masukkan harga baru: ")
    return price


def is_in(arr: Matrix, e: str, idx: int) -> bool:
    for i in range(len(arr)):
        if arr[i][idx] == e:
            return i
    return -1


def get_idx(data: Matrix, txt: str) -> str:
    idx: str = input(">>> Masukkan id %s: " % (txt))
    while not (is_number(idx) and is_in(data, idx, 0) != -1):
        if not is_number(idx):
            print("Masukkan input bertipe Integer, coba lagi!")
        else:
            print("ID tidak ada dalam data!")
        print()
        idx = input(">>> Masukkan id %s: " % (txt))
    return idx


def show(c: str, user_data: Mapping) -> None:
    if c == 'monster':
        monster_to_print: Matrix = concat(
            user_data["monster.csv"], user_data["monster_shop.csv"])
        table_print(monster_to_print)
    elif c == 'potion':
        table_print(add_id(user_data["item_shop.csv"]))
