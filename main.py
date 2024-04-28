import os
import argparse
from typing import *
from src.MenuAndHelp import menu


def folder_verification(folder_name: str) -> bool:
    if not os.path.isdir(folder_name):
        print(f'Folder "{folder_name}" tidak ditemukan, silakan ulangi!')
        return False
    print(f'Folder {folder_name} ditemukan!')
    return True


parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description='Verifies if a folder exists.')
parser.add_argument('folder_name', nargs='?',
                    type=folder_verification,
                    help='Nama folder')
args: argparse.ArgumentParser = parser.parse_args()

if args.folder_name is None:
    print('Masukkan nama folder Anda.')
    print('usage: python main.py <nama_folder>')
else:
    menu()
