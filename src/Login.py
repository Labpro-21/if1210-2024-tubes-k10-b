from typing import TextIO, List, Tuple
from .helper.Splitter import splitter
from .helper.ListManipulation import to_list, readlines

type Matrix = List[List[str]]


def verification(user: str, password: str, user_data: Matrix) -> Tuple[List[str], int]:
    for row in user_data:
        if user == row[1] and password == row[2]:
            arr: List[str] = []
            for i in row:
                arr.append(i)
            print("You are logged in as", end=" ")
            if "Admin" == row[3]:
                print('Admin!')
                return (arr, 0)
            print('Agent!')
            return (arr, 1)
        elif user == row[1] and password != row[2]:
            print('Wrong password, try again!')
            return ([], 1)

    print("Username doesn't exist!")
    return ([], 3)


def login(user_data: Matrix) -> int:
    '''
    0: admin
    1: verified user (non-admin)
    2: wrong password
    3: no user is registered
    '''
    user: str = input('Masukkan username Anda: ')
    password: str = input('Masukkan password Anda: ')

    return verification(user, password, user_data)
