from app.Tools.Tools import Tools

class InvoiceController:
    def index(self):
        border = "+----------------------------------------------------------+"
        border_len = len(border)
        print(border)
        print("| Menu Invoice" + " " * (border_len - len("| Menu Invoice ")) + "|" )
        print(border)
        print("|   1   | Cari Invoice" + " " * (border_len - len("|   1   | Cari Invoice ")) + "|")
        print("|   0   | Menu Utama" + " " * (border_len - len("|   0   | Menu Utama ")) + "|")
        print(border)
        user_input = Tools.validate_number_input("Tekan 1 untuk cari invoice dan 0 untuk kembali : ")
        if(user_input == 1):
            invoice_id = Tools.validate_number_input("Masukkan id invoice : ")
            InvoiceController.get_invoice(invoice_id, self)
        if(user_input == 0):
            Tools.clear()
            print(print("""
                                                Loading ...
            """))
            Tools.sleep(2)
        else:
            print("Pilihan menu tidak ada!")
            Tools.sleep(2)
            Tools.clear()
            InvoiceController.index(self)

    def get_invoice(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM invoices WHERE id = {}".format(self))

        rows = cur.fetchall()

        InvoiceController.print_invoice_data(rows, self)

    def print_invoice_data(self, invoice_id):
        border = "+-----------------------------------------------------------------------------------------------------------+"
        if (len(self) == 0):
            print( "    " + border)
            print( "    |" + " " * 35 + " Invoice dengan id  {} tidak ditemukan".format(invoice_id) + " " * 35 + "|")
            print( "    " + border)
            return
        print('''
    {}
    | Kode   | Nama              | Harga                 | Created At               | Updated At                |
    | Menu   | Menu              |                       |                          |                           |
    {}'''.format(border, border) )

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