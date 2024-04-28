from .helper.Splitter import splitter
from typing import TextIO, List


def is_valid(s: str) -> bool:
    '''
    [A-Z],[a-z], [_], [-] are allowed
    '''
    for i in s:
        if not (ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9') or i == '_' or i == '-'):
            return False
    return True


def verification(user: str) -> bool:
    '''
    0: username is not valid
    1: username is not available
    2: user completely registered
    '''
    if not is_valid(user):
        return 0
    user_data: TextIO = open('./data/user.csv', 'r')
    for i in user_data.readlines():
        data: List[str] = splitter(i)
        if data[1] == user:
            user_data.close()
            return 1
    user_data.close()
    return 2


def pick_monster(user_id: int, user: str) -> None:
    monster_data: TextIO = open('./data/monster.csv', 'r')
    data: List[str] = monster_data.readlines()
    n: int = len(data)
    print('\nSilakan pilih salah satu monster sebagai monster awalmu.')
    for i in range(1, n):
        splitted_data: List[str] = splitter(data[i])
        print("%s. %s" % (splitted_data[0], splitted_data[1]))
    monster_data.close()

    is_id_valid: bool = False
    while not is_id_valid:
        monster_id: str = input("\nID monster pilihanmu: ")
        for i in range(1, n):
            splitted_data: List[str] = splitter(data[i])
            if splitted_data[0] == monster_id:
                monster_inventory_data: TextIO = open(
                    './data/monster_inventory.csv', 'a')
                monster_inventory_data.write(
                    "%d;%s;%d\n" % (user_id, monster_id, 1))
                monster_inventory_data.close()
                print('\nSelamat datang Agent %s. Mari kita mengalahkan Dr. Asep Spakbor dengan %s!' % (
                    user, splitted_data[1]))
                return
        print('ID monster tidak ditemukan, silakan ulangi!')


def add_user(user: str, pw: str) -> None:
    user_data: TextIO = open('./data/user.csv', 'r')
    data: List[str] = user_data.readlines()
    last_id: int = int(data[len(data)-1][0])
    user_data.close()

    user_data: TextIO = open('./data/user.csv', 'a')
    user_data.write("%d;%s;%s;%s;%d\n" % (last_id+1, user, pw, "Agent", 0))
    user_data.close()

    pick_monster(last_id+1, user)


def regist() -> None:
    user: str = input("Masukan username: ")
    pw: str = input("Masukan password: ")
    verif: int = verification(user)
    if verif == 0:
        print('Username hanya boleh berisi alfabet, angka, underscore, dan strip!')
    elif verif == 1:
        print('Username %s sudah terpakai, silahkan gunakan username lain!' % (user))
    elif verif == 2:
        add_user(user, pw)
