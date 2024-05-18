def help_message_agent(username: str):
    print("=========== HELP ===========\n")

    print("Halo Agent %s. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:" % (username))

    print("Menu yang tersedia:")
    print("[HELP]\t\tMembantu untuk melihat command yang ada")
    print("[INVENTORY]\tUser melihat penyimpanan")
    print("[SHOP]\t\tUser Agent membeli monster dan potion")
    print("[LABORATORY]\tAgent melakukan upgrade monster")
    print("[ARENA]\t\tAgent melatih monster")
    print("[BATTLE]\tAgent melakukan battle")
    print("[LOGOUT]\tAgent melakukan logout akun")
    print("[SAVE]\t\tAgent melakukan save progres")
    print("[EXIT]\t\tUser keluar dari game")
    print()


def help_message_admin():
    print("=========== HELP ===========\n")
    print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
    print("Menu yang tersedia:")
    print("[HELP]\t\tMembantu untuk melihat command yang ada")
    print("[SHOP]\t\tAdmin mengatur manajemen Shop and Currency")
    print("[MONSTER]\tAdmin mengatur manajemen Monster")
    print("[SAVE]\t\tAdmin melakukan save progres")
    print("[LOGOUT]\tAdmin melakukan logout akun")
    print("[EXIT]\t\tAdmin keluar dari game")


def help_message_before_login():
    print("=========== HELP ===========\n")
    print("Kamu belum login sebagai role apapun. Silakan login terlebih dahulu.")
    print("Menu yang tersedia:")
    print("[HELP]\t\tMembantu untuk melihat command yang ada")
    print("[REGISTER]\tUser melakukan registrasi akun")
    print("[LOGIN]\t\tUser melakukan login akun")
    print("[EXIT]\t\tGuest keluar dari game")
