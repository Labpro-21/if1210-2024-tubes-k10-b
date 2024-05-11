from src.Save import save
from typing import List, Dict

type Matrix = List[List[str]]
type Mapping = Dict[str, Matrix]

def leave(data: Mapping) -> None:
    choice = input(
        'Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
    if choice.lower() == 'y':
        save(data)
    else:
        if choice.lower() != 'n':
            leave(data)
