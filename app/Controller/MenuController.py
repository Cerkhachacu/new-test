from app.Tools.Tools import Tools

class MenuController:
    def print_menu_data(self):
        print('''
    +-----------------------------------------------------------------------------------------------------------+
    | Kode   | Nama              | Harga                 | Created At               | Updated At                |
    | Menu   | Menu              |                       |                          |                           |
    +-----------------------------------------------------------------------------------------------------------+''' )
        if (len(self) == 0):
            print( "    |" + " " * 45 + " Data Kosong" + " " * 46 + "|")
            print( "    +-----------------------------------------------------------------------------------------------------------+")

        for i in range(len(self)):
            money_format = "{:,.0f}"

            menu_id = str(self[i][0]) + (" " * (6 - len(str(self[i][0]))))

            # field length 16 char
            menu_name = self[i][1] + (" " * (17 - len(self[i][1])))

            # field length 21 char
            price = "Rp. " + money_format.format(self[i][2]) + ( " " * (21 - len("Rp. " + money_format.format(self[i][2]))))

            
            # field length 21 char
            created_at = self[i][3] + (" " * (24 - len(self[i][3])))

            updated_at = self[i][4] + (" " * (25 - len(self[i][4])))

            print("    | " + menu_id + " | " + menu_name + " | " + price +
            " | " + created_at + " | " + updated_at + " | ")
            print("    +-----------------------------------------------------------------------------------------------------------+")
        print()

    def get_menu_data(self):
        cur = self.cursor()
        cur.execute("SELECT * FROM menus")

        rows = cur.fetchall()

        MenuController.print_menu_data(rows)

        print("""
    Atur Menu:
        1. Tambah Menu
        2. Update Menu
        3. Delete Menu
        0. Kembali ke home
        """)
        user_input = int(input("    Masukkan pilihan kamu: "))

        if user_input != 0:
            print("Masih di menu ini")
            Tools.sleep(2)
            Tools.clear()
            MenuController.get_menu_data(self)
        else:
            Tools.clear()
