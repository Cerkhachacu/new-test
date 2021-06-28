from app.Tools.Tools import Tools
import json
from app.Config.Connect import Connect
from app.Controller.MenuController import MenuController
from app.Controller.HomeController import HomeController
from app.Controller.InvoiceController import InvoiceController

conn = Connect.instance_method()

HomeController.show_header()
Tools.sleep(2)
Tools.clear()

def main():
    HomeController.show_menus()

    a = Tools.validate_number_input()
    if(a == 1):
        Tools.clear()
        MenuController.get_menu_data(conn)
        Tools.clear()
        main()

    if(a == 2):
        cur = conn.cursor()
        cur.execute("SELECT * FROM menus")

        rows = cur.fetchall()

        print(json.dumps(rows))
        
        Tools.sleep(2)
        Tools.clear()
        main()

    if(a == 3):
        Tools.clear()
        InvoiceController.index(conn)
        Tools.clear()
        main()
    
    else:
        print("Pilihan menu tidak ada!")
        Tools.sleep(2)
        Tools.clear()
        main()
main()