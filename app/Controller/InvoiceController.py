import json
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
            Tools.clear()
            InvoiceController.index(self)
        if(user_input != 0):
            print("Pilihan menu tidak ada!")
            Tools.sleep(1)
            Tools.clear()
            InvoiceController.index(self)
        else:
            Tools.clear()
            print("                                    Loading ...                               ")
            Tools.sleep(1)

    def get_invoice(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT invoices.id, menus.name, menus.price, invoice_details.qty, invoices.total FROM invoices LEFT JOIN invoice_details ON invoices.id = invoice_details.invoice_id LEFT JOIN menus ON menus.id = invoice_details.menu_id WHERE invoices.id = {}".format(self))

        rows = cur.fetchall()

        InvoiceController.print_invoice_data(rows, self)

    def print_invoice_data(self, invoice_id):
        border = "+---------------------------------------------------------------------------------------------------+"
        if (len(self) == 0):
            print( "    " + border)
            print( "    |" + " " * 35 + " Invoice dengan id  {} tidak ditemukan".format(invoice_id) + " " * 35 + "|")
            print( "    " + border)
            return
        print('''
    {}
    | Kode    | Nama              | Harga                 | Qty             | Total harga per pesanan   |
    | Invoice | Menu              |                       |                 |                           |
    {}'''.format(border, border) )

        for i in range(len(self)):
            money_format = "{:,.0f}"

            invoice_id = str(self[i][0]) + (" " * (7 - len(str(self[i][0]))))

            # field length 16 char
            menu_name = self[i][1] + (" " * (17 - len(self[i][1])))

            # field length 21 char
            price = "Rp. " + money_format.format(self[i][2]) + ( " " * (20 - len("Rp. " + money_format.format(self[i][2]))))

            
            # field length 21 char
            qty = str(self[i][3])
            qty = qty + (" " * (16 - len(qty)))

            total_per_menu = self[i][3] * self[i][2]
            total_per_menu = "Rp. " + money_format.format(total_per_menu) + ( " " * (25 - len("Rp. " + money_format.format(total_per_menu))))


            print("    | " + invoice_id + " | " + menu_name + " | " + price +
            " | " + qty + " | " + total_per_menu + " | ")
            print("    " + border)
        total = "Rp. " + money_format.format(self[i][4]) + ( " " * (25 - len("Rp. " + money_format.format(self[i][4]))))
        print("    |                                                          Total Bayar  | {} |".format(total))
        print("    " + border)
        print()
        input("    Tekan Enter jika sudah selesai ...")