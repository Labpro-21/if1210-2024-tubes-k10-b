import os
import time
import sys
from typing import List, Dict, TextIO
from .helper.ListManipulation import join

type Matrix = List[List[str]]
type Mapping = Dict[str, Matrix]


def pprint(folder_name: str, c: int = 2) -> None:
    def delayed_print(s: str) -> None:
        for i in s:
            print(i, end="")
            sys.stdout.flush()
            time.sleep(0.05)
        for i in "...":
            print(i, end="")
            sys.stdout.flush()
            time.sleep(0.75)
    delayed_print("Saving")
    print()
    print()
    if c == 0:
        delayed_print("Membuat folder data")
        print()
    elif c <= 1:
        delayed_print("Membuat folder data/%s" % (folder_name))
    print()
    print("Berhasil menyimpan data di folder data/%s!" % (folder_name))

def write_lines(file_name: str, folder_name: str, user_data: Mapping) -> None:
    f: TextIO = open("./data/%s/%s" % (folder_name, file_name), 'w')
    data_to_write: str = ""
    for row in user_data[file_name]:
        data_to_write += join(row) + "\n"
    f.write(data_to_write)
    f.close()

def save(user_data: Mapping) -> None:
    folder_name: str = input("Masukkan nama folder: ")
    print()
    if not os.path.isdir("./data"):
        pprint(folder_name, 0)
        os.makedirs("if1210-2024-tubes-k10-b/data")
    elif not os.path.isdir("./data/%s" % (folder_name)):
        pprint(folder_name, 1)
        os.makedirs("./data/%s" % (folder_name))
    elif os.path.isdir("./data/%s" % (folder_name)):
        pprint(folder_name)
    for file_name in user_data:
        write_lines(file_name, folder_name, user_data)
        
