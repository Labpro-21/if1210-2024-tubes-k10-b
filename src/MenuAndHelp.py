from src.Register import regist
from src.Login import login
from src.MonsterManagement import monster_management
from src.Logout import logout
from src.Help import help_message_agent, help_message_admin, help_message_before_login
from src.ShopManagement import shop_management
from src.Inventory import inventory
from typing import List

def menu(folder_name: str) -> None:
    is_login: bool = False
    is_logout: bool = False
    is_admin: bool = False
    user_data: List[str] = []
    print('\nLoading...')
    print("Ketik HELP untuk melihat command yang tersedia!")
    while not is_logout:
        choice: str = input("\n>>> ")
        if choice == "HELP":
            if is_admin:
                help_message_admin()
            elif is_login:
                help_message_agent()
            else:
                help_message_before_login()
        elif choice == "REGISTER":
            regist(folder_name)
        elif choice == "LOGIN":
            if is_login:
                print('You have been logged in!')
            else:
                result = login(folder_name)
                if result[1] <= 1:
                    is_login = True
                    user_data = result[0]
                if result[1] == 0:
                    is_admin = True
        elif choice == "INVENTORY" and is_login and not is_admin:
            inventory(user_data, folder_name)
        elif choice == "MONSTER" and is_login:
            if is_admin:
                monster_management(folder_name)
            else:
                print("Maaf, Anda bukan Admin!")
        elif choice == "SHOP":
            if is_admin:
                shop_management(folder_name)
            else:
                print("Maaf, Anda bukan Admin!")
        elif choice == "LOGOUT":
            logout(is_login)
            if is_login:
                is_logout = True
