import os
import argparse
from src.MenuAndHelp import menu


def load() -> None:
    def folder_verification(folder_name: str) -> bool:
        return os.path.isdir("./data/%s" % (folder_name))

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Verifies if a folder exists.')
    parser.add_argument('folder_name', nargs='?',
                        help='Nama folder')
    args: argparse.ArgumentParser = parser.parse_args()

    folder_name: str = args.folder_name
    if folder_name is None:
        print('Masukkan nama folder Anda.')
        print('usage: python main.py <nama_folder>')
    elif not folder_verification(args.folder_name):
        print('Folder %s tidak ditemukan, silakan ulangi!' % (folder_name))
    else:
        print('Folder %s ditemukan!' % (folder_name))
        menu(folder_name)
