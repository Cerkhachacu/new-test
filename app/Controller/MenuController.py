from app.Tools.Tools import Tools

class MenuController:
    def index(self):
        MenuController.get_menu_data(self)
        print("""
    Atur Menu:
        1. Tambah Menu
        2. Hapus Menu
        0. Kembali ke home
        """)
        user_input = int(input("    Masukkan pilihan kamu: "))

        if user_input == 0:
            Tools.sleep(1)
            print("                                    Loading ...                               ")
            Tools.clear()
            return

        if user_input == 1:
            Tools.clear()
            MenuController.add(self)
            Tools.clear()
            MenuController.index(self)
        
        if user_input == 2:
            Tools.clear()
            MenuController.delete(self)
            Tools.clear()
            MenuController.index(self)
        
        if user_input not in [0,1,2]:
            print('    Menu tidak ditemukan')
            Tools.sleep(1)
            Tools.clear()
            MenuController.index(self)


    def print_menu_data(self, is_master):
        header = '''
    +-----------------------------------------------------------------------------------------------------------+
    | Kode   | Nama              | Harga                 | Created At               | Updated At                |
    | Menu   | Menu              |                       |                          |                           |
    +-----------------------------------------------------------------------------------------------------------+'''
        border = "+-----------------------------------------------------------------------------------------------------------+"
        if(is_master != 0):
            header = '''
    +----------------------------------------------------+
    | Kode   | Nama              | Harga                 |
    | Menu   | Menu              |                       |
    +----------------------------------------------------+'''
            border = "+----------------------------------------------------+"
            
        print(header)
        if (len(self) == 0):
            space_if_empty =  " " * 45 + " Data Kosong" + " " * 46 + "|"
            if(is_master != 0):
                space_if_empty = " " * 20 + " Data Kosong " + " " * 20 + "|"
            print( "    |" + space_if_empty)
            print( "    " + border)

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

            data = menu_id + " | " + menu_name + " | " + price + " | " + created_at + " | " + updated_at + " | "
            if(is_master != 0 ):
                data = menu_id + " | " + menu_name + " | " + price + " | "

            print("    | " + data)
            print("    " + border)
        print()

    def get_menu_data(self, is_master=0):
        cur = self.cursor()
        cur.execute("SELECT * FROM menus")

        rows = cur.fetchall()

        MenuController.print_menu_data(rows, is_master)

    def add(self):
        cur = self.cursor()
        print("    ~Tambah menu baru~")
        print("    Tekan 0 untuk kembali")

        name = input("    Masukkan nama menu: ")
        if name == "0":
            return

        price = Tools.validate_number_input("    Masukkan harga: Rp. ")

        sql = "INSERT INTO menus(name, price) VALUES(?,?)"
        cur.execute(sql, [name, price])

        self.commit()

        print("    Menu baru berhasil ditambahkan ...")
        Tools.sleep(1)

    def delete(self):
        cur = self.cursor()
        print("    ~Hapus Menu~")
        print("    Tekan 0 untuk kembali")

        menu_id = Tools.validate_number_input("    Masukkan id menu: ")

        if menu_id == 0:
            return

        cur.execute("SELECT * from menus WHERE id = {}".format(menu_id))

        row = cur.fetchall()

        if len(row) == 0:
            print("    Menu dengan id yang dimasukkan tidak ditemukan.")
            Tools.sleep(1)
            Tools.clear()
            MenuController.delete(self)
        
        cur.execute("DELETE FROM menus WHERE id = {}".format(menu_id))

        self.commit()

        print("    Menu berhasil dihapus.")
        Tools.sleep(1)