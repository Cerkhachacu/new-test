from app.Config import Connect

class MenuSeeder:
    def instance_method(self='seed'):
        print("Seeding menu")
        conn = Connect.instance_method()
        print("Opened database successfully")

        cur = conn.cursor()

        sql = ''' INSERT INTO menus(name, price)
              VALUES(?,?) '''
        cur.executemany(sql, [('Menu A', 2000), ('Menu B', 4000), ('Menu C', 8000), ('Menu D', 16000)])
        conn.commit()

        conn.close()
        print("Menu seeding succesfully")