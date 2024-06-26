from src.Register import regist
from src.Login import login
from src.MonsterManagement import monster_management
from src.Logout import logout
from src.Help import help_message_agent, help_message_admin, help_message_before_login
from src.ShopManagement import shop_management
from src.Inventory import inventory
from src.Exit import leave
from src.Battle import battle
from src.ShopAndCurrency import shop_and_currency
from src.Laboratory import laboratory
from src.Save import save
from src.Arena import arena
from typing import List, Dict
from .helper.ListManipulation import read_all
import os

Matrix = List[List[str]]
Mapping = Dict[str, Matrix]


def menu(folder_name: str) -> None:
    is_login: bool = False
    is_exit: bool = False
    is_admin: bool = False
    user_data: Mapping = {}
    user_login: List[str] = []
    read_all(user_data, folder_name)
    print('\nLoading...')
    print("Ketik HELP untuk melihat command yang tersedia!")
    while not is_exit:
        choice: str = input("\n>>> ")
        if choice == "HELP":
            if is_admin:
                help_message_admin()
            elif is_login:
                help_message_agent(user_login[1])
            else:
                help_message_before_login()
        elif choice == "REGISTER":
            if is_login:
                print("Register gagal!")
                print("Anda telah login dengan username %s, silahkan lakukan “LOGOUT” sebelum melakukan register." % (
                    user_login[1]))
            else:
                regist(user_data)
        elif choice == "LOGIN":
            if is_login:
                print('You have been logged in!')
            else:
                result = login(user_data["user.csv"])
                if result[1] <= 1:
                    is_login = True
                    user_login = result[0]
                if result[1] == 0:
                    is_admin = True
        elif choice == "INVENTORY" and is_login and not is_admin:
            inventory(user_login, user_data)
        elif choice == "MONSTER" and is_admin:
            monster_management(user_data)
        elif choice == "SHOP":
            if is_admin:
                shop_management(user_data)
            elif is_login:
                shop_and_currency(user_data, user_login)
        elif choice == "LABORATORY" and is_login and not is_admin:
            laboratory(user_login, user_data)
        elif choice == "BATTLE" and is_login and not is_admin:
            battle(user_login, user_data, 0, "null", 0, 0, 0, 0, 0, 0, 1)
        elif choice == "LOGOUT":
            logout(is_login)
            if is_login:
                is_login = False
                is_admin = False
        elif choice == "EXIT":
            is_exit = True
            leave(user_data)
        elif choice == "ARENA" and is_login and not is_admin:
            arena(user_login, user_data, 1, 1, 0, 0, "null", 0, 0, 0, 0, 1)
        elif choice == "SAVE":
            save(user_data)
