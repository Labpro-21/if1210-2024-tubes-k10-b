from src.Save import save
from typing import List

type Vector = List[List[str]]

def leave(data: Vector) -> None:
    choice = input(
        'Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
    if choice.lower() == 'y':
        save(data)
    else:
        if choice.lower() != 'n':
            leave(data)
