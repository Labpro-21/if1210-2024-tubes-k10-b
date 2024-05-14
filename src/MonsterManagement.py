from typing import TextIO, List, Dict
from .helper.Splitter import splitter
from .helper.IsType import is_number
from .helper.ListManipulation import table_print, to_list, readlines

Matrix = List[List[str]]
Mapping = Dict[str, Matrix]


def get_type(user_data: Mapping) -> str:
    def is_added(name) -> bool:
        monster_data: Matrix = user_data["monster.csv"]
        for row in monster_data:
            if name == row[1]:
                return True
        return False

    name: str = input(">>> Masukkan Type / Nama: ")
    while is_added(type):
        print("Nama sudah terdaftar, coba lagi!")
        print()
        name: str = input(">>> Masukkan Type / Nama: ")
    return name


def get_atk_power() -> str:
    atk_power = input(">>> Masukkan ATK Power: ")
    while not is_number(atk_power):
        print("Masukkan input bertipe Integer, coba lagi!")
        print()
        atk_power = input(">>> Masukkan ATK Power: ")
    return atk_power


def get_def_power() -> str:
    def is_valid(def_power) -> bool:
        if not is_number(def_power):
            return False
        if not (0 <= int(def_power) <= 50):
            return False
        return True

    def_power: str = input(">>> Masukkan DEF Power (0-50): ")
    while not is_valid(def_power):
        if not is_number(def_power):
            print("Masukkan input bertipe Integer, coba lagi!")
        elif not (0 <= int(def_power) <= 50):
            print("DEF Power harus bernilai 0-50, coba lagi!")
        print()
        def_power: str = input(">>> Masukkan DEF Power (0-50): ")
    return def_power


def get_hp() -> str:
    hp: str = input(">>> Masukkan HP: ")
    while not is_number(hp):
        print("Masukkan input bertipe Integer, coba lagi!")
        print()
        hp: str = input(">>> Masukkan HP: ")
    return hp


def get_last_id(user_data: Mapping) -> int:
    data: Matrix = user_data["monster.csv"]
    last_id: int = data[len(data)-1][0]
    return int(last_id)


def add_monster(user_data: Mapping) -> None:
    print("Memulai pembuatan monster baru")
    print()

    idn: int = get_last_id(user_data)
    name: str = get_type(user_data)
    atk_power: str = get_atk_power()
    def_power: str = get_def_power()
    hp: str = get_hp()

    print("Monster baru berhasil dibuat!")
    print("Type:", name)
    print("ATK Power:", atk_power)
    print("DEF Power:", def_power)
    print("HP:", hp)

    choice: str = input("Tambahkan Monster ke database (Y/N): ")
    while choice.upper() != 'Y' and choice.upper() != 'N':
        choice: str = input("Tambahkan Monster ke database (Y/N): ")
    if choice.upper() == 'Y':
        user_data["monster.csv"].append([str(idn+1), name, atk_power, def_power, hp])
        print("Monster baru telah ditambahkan!")


def monster_management(user_data: Mapping) -> None:
    print("SELAMAT DATANG DI DATABASE PARA MONSTER!!!")
    print("1. Tampilkan semua Monster")
    print("2. Tambah Monster baru")
    choice = input(">>> Pilih aksi: ")
    if choice == '1':
        table_print(user_data["monster.csv"])
    elif choice == '2':
        add_monster(user_data)
    else:
        monster_management(user_data)
