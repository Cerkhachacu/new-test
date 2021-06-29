class AboutController:
    def index(self="about"):
        border = "+----------------------------------------------------------+"
        border_len = len(border)
        print("Kelompok 3")
        print(border)
        print("| NIK      | NAMA" + " " * (border_len - len("| NIK      | NAMA ")) + "|" )
        print(border)
        print("| 19207079 | Aprilia Rizki" + " " * (border_len - len("| 19207xxx | Aprilia Rizki ")) + "|")
        print("| 19207162 | Arda Gracio" + " " * (border_len - len("| 19207xxx | Arda Gracio ")) + "|")
        print("| 19207242 | Farid Hidayat" + " " * (border_len - len("| 19207xxx | Farid Hidayat ")) + "|")
        print("| 19207197 | Indra Setiawan" + " " * (border_len - len("| 19207xxx | Indra setiawan ")) + "|")
        print("| 19207229 | Syahrul Rahman" + " " * (border_len - len("| 19207xxx | Syahrul Rahman ")) + "|")
        print("| 19207046 | Tri Robby Hartanto" + " " * (border_len - len("| 19207xxx | Tri Robby Hartanto ")) + "|")
        print("| 19207214 | Yanral Apdy" + " " * (border_len - len("| 19207xxx | Yanral Apdy ")) + "|")
        print(border)

        input("Tekan tombol Enter untuk kembali ... ")
