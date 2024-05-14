from .helper.Splitter import splitter
from typing import TextIO, List, Dict
from .helper.ListManipulation import to_list, readlines

Matrix = List[List[str]]
Mapping = Dict[str, Matrix]


def is_valid(s: str) -> bool:
    '''
    [A-Z],[a-z], [_], [-] are allowed
    '''
    for i in s:
        if not (ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9') or i == '_' or i == '-'):
            return False
    return True


def verification(user: str, user_data: Matrix) -> bool:
    '''
    0: username is not valid
    1: username is not available
    2: user completely registered
    '''
    if not is_valid(user):
        return 0
    for data in user_data:
        if data[1] == user:
            return 1
    return 2


def pick_monster(user_id: int, user: str, user_data: Mapping) -> None:
    data: Matrix = user_data["monster.csv"]
    n: int = len(data)
    print('\nSilakan pilih salah satu monster sebagai monster awalmu.')
    for i in range(1, n):
        print("%s. %s" % (data[i][0], data[i][1]))

    while True:
        monster_id: str = input("\nID monster pilihanmu: ")
        for i in range(1, n):
            if data[i][0] == monster_id:
                user_data["monster_inventory.csv"].append([str(user_id), monster_id, "1"])
                print('\nSelamat datang Agent %s. Mari kita mengalahkan Dr. Asep Spakbor dengan %s!' % (
                    user, data[i][1]))
                return
        print('ID monster tidak ditemukan, silakan ulangi!')


def add_user(user: str, pw: str, user_data: Mapping) -> None:
    data: Matrix = user_data["user.csv"]
    last_id: int = int(data[len(data)-1][0])
    user_data["user.csv"].append([str(last_id+1), user, pw, "Agent", "0"])
    
    pick_monster(last_id+1, user, user_data)


def regist(user_data: Matrix) -> None:
    user: str = input("Masukan username: ")
    pw: str = input("Masukan password: ")
    verif: int = verification(user, user_data["user.csv"])
    if verif == 0:
        print('Username hanya boleh berisi alfabet, angka, underscore, dan strip!')
    elif verif == 1:
        print('Username %s sudah terpakai, silahkan gunakan username lain!' % (user))
    elif verif == 2:
        add_user(user, pw, user_data)
