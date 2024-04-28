def logout(is_login: bool) -> None:
    if not is_login:
        print("Logout gagal!")
        print("Anda belum login, silakan login terlebih dahulu sebelum melakukan logout")