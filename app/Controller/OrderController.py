from app.Tools.Tools import Tools
from app.Controller.MenuController import MenuController
import json

class OrderController:
    def index(self):
        print("    ~Menu Pemesanan~")
        MenuController.get_menu_data(self, 1)
        print("""
    Ready for order :
        1. Order
        0. Kembali ke home
        """)
        user_input = int(input("    Masukkan pilihan kamu: "))
        if user_input == 1:
            return OrderController.order(self)

        if user_input == 0:
            Tools.clear()
            print("                                    Loading ...                               ")
            Tools.sleep(1)
            Tools.clear()
            
        if user_input not in [0,1]:
            print("Pilihan menu tidak ada!")
            Tools.sleep(1)
            Tools.clear()
            return OrderController.index(self)

    def order(self):
        print()
        cur = self.cursor()
        cur.execute("SELECT id, price, name FROM menus")

        rows = cur.fetchall()

        menu_ids = []
        menus = {}
        for a in rows:
            menu_ids.append(a[0])
            menus[a[0]] = [a[1], a[2]]

        print('    Input angka 0 (nol) jika sudah selesai melakukan pesanan.')
        orders = OrderController.place_order(menu_ids, {})

        orders_record = []
        total_price = 0
        response = {'data': {'menus': {}}}
        for key in orders:
            orders_record.append([int(key), orders[key]])
            total_price += menus[key][0] * orders[key]
            response['data']['menus'][menus[key][1]] = orders[key]

        response['data']['total_harga'] = total_price

        invoice_id = OrderController.insert_invoice_and_invoice_detail_record(self, orders_record, total_price)
        
        response['data']['invoid_id'] = invoice_id

        print(json.dumps(response, indent=4, sort_keys=True))

        print('\nSimpan invoice id!')
        input("Tekan tombol Enter untuk kembali ... ")

        Tools.sleep(1)
        Tools.clear()
        OrderController.index(self)

    def place_order(self, orders):
        menu_id = Tools.validate_number_input('    Masukkan menu id atau 0 jika sudah selesai order : ')

        if menu_id == 0:
            return orders
        if menu_id not in self:
            print('    Tidak ada menu dengan id tersebut')
            return OrderController.place_order(self, orders)
        
        qty = Tools.validate_number_input('    Masukkan jumlah pesanan : ', 1, '    Jumlah pesanan harus lebih besar dari 0 ')
        print('    menu ditambahkan ke order')
        if menu_id in orders:
            orders[menu_id] += qty
        else:
            orders[menu_id] = qty
        
        return OrderController.place_order(self, orders)

    def insert_invoice_and_invoice_detail_record(self, orders_data, total_price):
        cur = self.cursor()
        sql = ''' INSERT INTO invoices(total)
              VALUES(?) '''

        cur.execute(sql, [total_price])
        invoice_id = cur.lastrowid

        invoice_details = []
        for menu in orders_data:
            invoice_details.append([menu[0], menu[1], invoice_id])

        sql = ''' INSERT INTO invoice_details(menu_id, qty, invoice_id)
              VALUES(?,?,?) '''

        cur.executemany(sql, invoice_details)
        self.commit()
        return invoice_id