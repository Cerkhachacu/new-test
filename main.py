from app.Tools.Tools import Tools
from app.Config.Connect import Connect
from app.Controller.MenuController import MenuController
from app.Controller.HomeController import HomeController
from app.Controller.InvoiceController import InvoiceController
from app.Controller.AboutController import AboutController
from app.Controller.OrderController import OrderController

conn = Connect.instance_method()

HomeController.show_header()
Tools.sleep(1)
Tools.clear()

def main():
    HomeController.show_menus()

    a = Tools.validate_number_input()
    if(a == 1):
        Tools.clear()
        MenuController.index(conn)
        Tools.clear()
        main()

    if(a == 2):
        Tools.clear()
        OrderController.index(conn)
        Tools.clear()
        main()

    if(a == 3):
        Tools.clear()
        InvoiceController.index(conn)
        Tools.clear()
        main()
    
    if(a == 4):
        Tools.clear()
        AboutController.index()
        Tools.clear()
        main()

    if(a == 0):
        Tools.clear()
        print("                                    Quiting ...                               ")
        Tools.sleep(2)
        Tools.clear()
        quit()

    else:
        print("Pilihan menu tidak ada!")
        Tools.sleep(2)
        Tools.clear()
        main()
        
main()