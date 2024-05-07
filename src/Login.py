from typing import TextIO, List, Tuple
from .helper.Splitter import splitter


def get_user(data: str) -> List[str]:
    return splitter(data)


def verification(user: str, password: str, folder_name: str) -> Tuple[List[str], int]:
    user_data: TextIO = open('./data/%s/user.csv' % (folder_name), 'r')
    for data in user_data.readlines():
        row: List[str] = get_user(data)
        if user == row[1] and password == row[2]:
            print("You are logged in as", end=" ")
            if "Admin" == row[3]:
                print('Admin!')
                return ([], 0)
            print('Agent!')
            return (row, 1)
        elif user == row[1] and password != row[2]:
            print('Wrong password, try again!')
            return ([], 1)

    user_data.close()
    print("Username doesn't exist!")
    return ([], 3)


def login(folder_name: str) -> int:
    '''
    0: admin
    1: verified user (non-admin)
    2: wrong password
    3: no user is registered
    '''
    user: str = input('Masukkan username Anda: ')
    password: str = input('Masukkan password Anda: ')

    return verification(user, password, folder_name)
