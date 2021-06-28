class HomeController:
    def show_header(self="home"): 
        return (
            print("""
            +------------------------------------------------------------------------------+
            
            ██   ██ ███████ ██       ██████  ███    ███ ██████   ██████  ██   ██     ██████  
            ██  ██  ██      ██      ██    ██ ████  ████ ██   ██ ██    ██ ██  ██           ██ 
            █████   █████   ██      ██    ██ ██ ████ ██ ██████  ██    ██ █████        █████  
            ██  ██  ██      ██      ██    ██ ██  ██  ██ ██      ██    ██ ██  ██           ██ 
            ██   ██ ███████ ███████  ██████  ██      ██ ██       ██████  ██   ██     ██████  
            +-------------------------------------------------------------------------------+

                                                Loading ...
            """)
        )

    def show_menus(self="home"):
        border = "+----------------------------------------------------------+"
        border_len = len(border)
        print("Selamat Datang")
        print(border)
        print("| Menu  | Menu Utama" + " " * (border_len - len("| Menu  | Menu Utama ")) + "|" )
        print(border)
        print("|   1   | Master Data Menu" + " " * (border_len - len("|   1   | Master Data Menu ")) + "|")
        print("|   2   | Pesan Makanan" + " " * (border_len - len("|   2   | Pesan Makanan ")) + "|")
        print("|   3   | Invoice Pembayaran" + " " * (border_len - len("|   3   | Invoice Pembayaran ")) + "|")
        print("|   4   | Tentang Aplikasi" + " " * (border_len - len("|   4   | Tentang Aplikasi ")) + "|")
        print("|   0   | Keluar" + " " * (border_len - len("|   0   | Keluar ")) + "|")
        print(border)
