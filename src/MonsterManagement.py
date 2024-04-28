from typing import TextIO, List
from .helper.Splitter import splitter
from .helper.IsType import is_number


def show() -> None:
    monster_data: TextIO = open('./data/monster.csv', 'r')
    print("ID\t| Type\t\t | ATK Power\t | DEF Power\t | HP")
    for data in monster_data.readlines():
        row = splitter(data)
        print(f"{row[0]}\t| {row[1]}\t | {row[2]}\t\t | {row[3]}\t | {row[4]}")
    monster_data.close()


def get_type() -> str:
    def is_added(name) -> bool:
        monster_data: TextIO = open('./data/monster.csv', 'r')
        for data in monster_data.readlines():
            row: List[str] = splitter(data)
            if name == row[1]:
                monster_data.close()
                return True
        monster_data.close()
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


def get_last_id() -> int:
    monster_data: TextIO = open('./data/monster.csv', 'r')
    data: List[str] = monster_data.readlines()
    last_id: int = data[len(data)-1][0]
    monster_data.close()
    return int(last_id)


def add_monster() -> None:
    print("Memulai pembuatan monster baru")
    print()

    idn: int = get_last_id()
    name: str = get_type()
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
        monster_data: TextIO = open('./data/monster.csv', 'a')
        monster_data.write("%s;%s;%s;%s;%s\n" %
                           (idn+1, name, atk_power, def_power, hp))
        monster_data.close()
        print("Monster baru telah ditambahkan!")


def monster_management() -> None:
    print("SELAMAT DATANG DI DATABASE PARA MONSTER!!!")
    print("1. Tampilkan semua Monster")
    print("2. Tambah Monster baru")
    choice = input(">>> Pilih aksi: ")
    if choice == '1':
        show()
    elif choice == '2':
        add_monster()
    else:
        monster_management()
