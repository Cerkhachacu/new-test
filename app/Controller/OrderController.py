from app.Tools.Tools import Tools
from app.Controller.MenuController import MenuController
import json

class OrderController:
    def index(self):
        MenuController.get_menu_data(self, 1)
        print("""
    Ready for order :
        1. Order
        0. Kembali ke home
        """)
        user_input = int(input("    Masukkan pilihan kamu: "))
        if(user_input == 1):
            OrderController.order(self)

        if(user_input == 0):
            Tools.clear()
            print("                                    Loading ...                               ")
            Tools.sleep(2)

        else:
            print("Pilihan menu tidak ada!")
            Tools.sleep(2)
            Tools.clear()
            OrderController.index(self)

    def order(self):
        print()
        cur = self.cursor()
        cur.execute("SELECT id FROM menus")

        rows = cur.fetchall()

        menu_ids = []
        for a in rows:
            menu_ids.append(a[0])
        
        a = input("    Masukkan menu id : ")
        Tools.sleep(2)
        Tools.clear()
        OrderController.index(self)