from typing import List, Dict
from .helper.ListManipulation import to_list
from src.ShopManagement import concat, lihat, get_idx, is_in, add_id
from .helper.IsType import is_number

Matrix = List[List[str]]
Mapping = Dict[str, Matrix]


def is_added(user_data: Matrix, user_id: str, idn: str) -> bool:
    for i in user_data:
        if i[0] == user_id and i[1] == idn:
            return True
    return False


def index_added_potion(potion_inventory: Matrix, potion_name: str, idn: str, user_id) -> int:
    for i, row in enumerate(potion_inventory):
        if row[0] == user_id and row[1] == potion_name:
            return i
    return -1


def beli(user_data: Mapping, user_login: List[str]) -> None:
    print("Jumlah O.W.C.A. Coin-mu sekarang %s.\n"
          % (user_login[4]))
    breaked: bool = False
    while not breaked:
        c: str = input(">>> Mau beli apa? (monster/potion): ")
        if c in ['monster', 'potion']:
            breaked: bool = True
    if c == 'monster':
        monster: Matrix = user_data["monster.csv"]
        monster_shop: Matrix = user_data["monster_shop.csv"]
        inventory: Matrix = user_data["monster_inventory.csv"]

        idn: str = get_idx(user_data['monster.csv'], 'monster')
        row_index: int = is_in(monster_shop, idn, 0)
        price: int = int(monster_shop[row_index][2])
        if monster_shop[row_index][1] == '0':
            print("Monster %s sedang tidak tersedia (kosong)." %
                  (monster[is_in(monster, idn, 0)][1]))
        elif is_added(inventory, user_login[0], idn):
            print("Monster %s sudah ada dalam inventory-mu! Pembelian dibatalkan." %
                  (monster[is_in(monster, idn, 0)][1]))
        elif int(user_login[4]) < price:
            print("OC-mu tidak cukup.")
        else:
            # mengurangi OC
            user_login[4] = str(int(user_login[4]) - price)
            # menambahkan ke inventory (isi di bawah)
            inventory.append([user_login[0], idn, '1'])
            # mengurangi pada shop
            monster_shop[row_index][1] = str(
                int(monster_shop[row_index][1]) - 1)
            print("Berhasil membeli item: %s. Item sudah masuk ke inventory-mu!" %
                  (monster[is_in(monster, idn, 0)][1]))
    elif c == "potion":
        potion: Matrix = user_data["item_shop.csv"]
        potion_inventory: Matrix = user_data["item_inventory.csv"]
        idn: str = get_idx(add_id(potion), 'potion')
        price: int = int(potion[int(idn)][2])

        def get_jumlah() -> str:
            cc: str = input(">>> Masukkan jumlah: ")
            while not is_number(cc):
                print("Masukkan input bertipe Integer, coba lagi!")
                print()
                cc: str = input(">>> Masukkan jumlah: ")
            return int(cc)
        jumlah: str = get_jumlah()
        if int(user_login[4]) < jumlah * price:
            print("OC-mu tidak cukup.")
        elif jumlah > int(potion[int(idn)][1]):
            print("Jumlah yang diminta melebihi stok.")
        else:
            # mengurangi stok pada shop
            potion[int(idn)][1] = str(int(potion[int(idn)][1]) - jumlah)
            # mengurangi OC
            user_login[4] = str(int(user_login[4]) - jumlah * price)
            # menambahkan ke inventory (isi di bawah)
            user_inventory_idx: int = index_added_potion(
                potion_inventory, potion[int(idn)][0], idn, user_login[0])
            if user_inventory_idx == -1:
                potion_inventory.append(
                    [user_login[0], potion[int(idn)][0], str(jumlah)])
            else:
                potion_inventory[user_inventory_idx][2] = str(
                    int(potion_inventory[user_inventory_idx][2]) + jumlah)
            print("Berhasil membeli item: %s Potion of %s. Item sudah masuk ke inventory-mu!" %
                  (jumlah, potion[int(idn)][0]))


def shop_and_currency(user_data, user_login):
    print("Irasshaimase! Selamat datang di SHOP!!")
    breaked: bool = False
    while not breaked:
        masukan: str = (input("\n>>> Pilih aksi (lihat/beli/keluar): "))
        if masukan.lower() == "lihat":
            lihat(user_data)
        elif masukan.lower() == "beli":
            beli(user_data, user_login)
        elif masukan.lower() == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            breaked = True
