from typing import TextIO, List
from .helper.Splitter import splitter
from .helper.ListManipulation import table_print, to_list, join
from .helper.Readline import readlines
from .helper.IsType import is_number


def lihat():
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c)
        if c in ['monster', 'potion']:
            breaked: bool = True


def tambah() -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        if c in ['monster', 'potion']:
            breaked = True
    if c == 'monster':
        contoh: List[List[str]] = [["ID", "Type", "ATK Power", "DEF Power", "HP"],
                                   ["4", "Cici", "10", "1000", "200"],
                                   ["5", "Moskov", "20", "1000", "200"],
                                   ["6", "Selena", "30", "430", "100"]]
        monster = to_list(readlines('./data/monster.csv'))
        arr = []
        for i in contoh:
            if is_in(monster, i[0], 0) == -1:
                arr.append(i)
        table_print(arr)
        idx: str = get_idx(arr, 'monster')
        stock: str = get_stock()
        price: str = get_price()
        monster: TextIO = open('./data/monster.csv', 'a')
        monster_shop: TextIO = open('./data/monster_shop.csv', 'a')
        idn: str = is_in(arr, idx, 0)
        monster.write("%s\n" % (join(arr[idn])))
        monster_shop.write("%s;%s;%s\n" % (arr[idn][0], stock, price))
        monster.close()
        monster_shop.close()
    elif c == 'potion':
        contoh: List[List[str]] = [["ID", "Type"],
                                   ["3", "Healing Potion"]]
        arr = []
        potion = to_list(readlines('./data/item_shop.csv'))
        for i in contoh:
            if is_in(potion, i[0], 0) == -1:
                arr.append(i)
        table_print(arr)
        idx: str = get_idx(arr, 'potion')
        stock: str = get_stock()
        price: str = get_price()
        potion: TextIO = open('./data/item_shop.csv', 'a')
        idn: str = is_in(arr, idx, 0)
        potion.write("%s;%s;%s\n" % (arr[idn][1], stock, price))
        potion.close()
    return


def ubah() -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c)
        if c in ['monster', 'potion']:
            breaked = True
    if c == 'monster':
        monster_shop: List[str] = readlines('./data/monster_shop.csv')
        monster: List[str] = readlines('./data/monster.csv')
        monster_list: List[List[str]] = concat(monster, monster_shop)
        idx: str = get_idx(monster_list, 'monster')
        stock: str = get_stock()
        price: str = get_price()
        txt_to_write: str = ""
        for i in range(len(monster_shop)):
            data = splitter(monster_shop[i])
            if data[0] == idx:
                if stock != "":
                    data[1] = stock
                if price != "":
                    data[2] = price
            txt_to_write += join(data) + '\n'
        write_it_out('./data/monster_shop.csv', txt_to_write)
    elif c == 'potion':
        potion: List[List[str]] = add_id(
            to_list(readlines('./data/item_shop.csv')))
        idx: str = get_idx(potion, 'potion')
        stock: str = get_stock()
        price: str = get_price()
        potion: List[str] = readlines('./data/item_shop.csv')
        txt_to_write: str = ""
        for i in range(len(potion)):
            data = splitter(potion[i])
            if i == int(idx):
                if stock != "":
                    data[1] = stock
                if price != "":
                    data[2] = price
            txt_to_write += join(data) + '\n'
        write_it_out('./data/item_shop.csv', txt_to_write)
    return


def hapus() -> None:
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau lihat apa? (monster/potion): ")
        show(c)
        if c in ['monster', 'potion']:
            breaked = True
    if c == 'monster':
        monster_shop: List[str] = readlines('./data/monster_shop.csv')
        monster: List[str] = readlines('./data/monster.csv')
        monster_list: List[List[str]] = concat(monster, monster_shop)
        idx: str = get_idx(monster_list, 'monster')
        if verification_hapus():
            write_without('./data/monster_shop.csv', idx)
            write_without('./data/monster.csv', idx)
    elif c == 'potion':
        potion: List[List[str]] = add_id(
            to_list(readlines('./data/item_shop.csv')))
        idx: str = get_idx(potion, 'potion')
        if verification_hapus():
            write_without('./data/item_shop.csv', idx, True)
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


def write_it_out(path: str, txt: str) -> None:
    data: TextIO = open(path, 'w')
    data.write(txt)
    data.close()


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


def add_id(data: List[List[str]]) -> List[List[str]]:
    row: int = len(data)
    col: int = len(data[0])
    arr: List[List[str]] = [["" for _ in range(col+1)] for _ in range(row)]
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


def write_without(path: str, idx: str, is_potion: bool = False) -> None:
    data: List[str] = readlines(path)
    data_2d: List[List[str]] = to_list(data)
    data_to_write: TextIO = open(path, 'w')
    txt_to_write: str = ""
    if is_potion:
        for i in range(len(data)):
            if i != int(idx):
                txt_to_write += data[i]
    else:
        for i in range(len(data)):
            if data_2d[i][0] != idx:
                txt_to_write += data[i]
    data_to_write.write(txt_to_write)
    data_to_write.close()


def verification_hapus() -> bool:
    is_hapus: str = ""
    while is_hapus.lower() not in ['y', 'n']:
        is_hapus: str = input(
            ">>> Apakah anda yakin ingin menghapus %s dari shop (y/n)? ")
    if is_hapus.lower() == 'y':
        return True
    return False


def get_stock() -> str:
    stock: str = input(">>> Masukkan stok baru: ")
    while not (is_number(stock)):
        print("Masukkan input bertipe Integer nonnegatif, coba lagi!\n")
        stock = input(">>> Masukkan stok baru: ")
    return stock


def get_price() -> str:
    price: str = input(">>> Masukkan harga baru: ")
    while not (is_number(price)):
        print("Masukkan input bertipe Integer nonnegatif, coba lagi!\n")
        price = input(">>> Masukkan harga baru: ")
    return price


def is_in(arr: List[List[str]], e: str, idx: int) -> bool:
    for i in range(len(arr)):
        if arr[i][idx] == e:
            return i
    return -1


def get_idx(data: List[List[str]], txt: str) -> str:
    idx: str = input(">>> Masukkan id %s: " % (txt))
    while not (is_number(idx) and is_in(data, idx, 0) != -1):
        if not is_number(idx):
            print("Masukkan input bertipe Integer, coba lagi!")
        else:
            print("ID tidak ada dalam data!")
        print()
        idx = input(">>> Masukkan id %s: " % (txt))
    return idx


def show(c: str) -> None:
    if c == 'monster':
        monster_shop: TextIO = readlines('./data/monster_shop.csv')
        monster: TextIO = readlines('./data/monster.csv')
        monster_to_print: List[str] = concat(monster, monster_shop)
        table_print(monster_to_print)
    elif c == 'potion':
        item_shop: TextIO = readlines('./data/item_shop.csv')
        table_print(add_id(to_list(item_shop)))