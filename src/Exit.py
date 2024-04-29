from src.Save import save


def leave(is_admin: bool) -> None:
    choice = input(
        'Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
    if choice.lower() == 'y':
        save(is_admin)
    else:
        if choice.lower() != 'n':
            leave()
