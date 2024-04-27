from typing import TextIO, List
from helper.Splitter import splitter


def get_user(data: str) -> List[str]:
    return splitter(data)


def verification(user: str, password: str) -> bool:
    user_data: TextIO = open('./data/user.csv', 'r')
    for data in user_data.readlines():
        row: List[str] = get_user(data)
        if user == row[1] and password == row[2]:
            if "Admin" == row[3]:
                return 0
            return 1
        elif user == row[0] and password != row[1]:
            return 2

    user_data.close()
    return 3


def login() -> int:
    '''
    0: admin
    1: verified user (non-admin)
    2: wrong password
    3: no user is registered
    '''
    user: str = input('Masukkan username Anda: ')
    password: str = input('Masukkan password Anda: ')

    return verification(user, password)