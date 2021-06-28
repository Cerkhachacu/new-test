class MenuSeeder:
    def instance_method(self='seed'):
        print("Seeding menu")

        cur = self.cursor()

        sql = ''' INSERT INTO menus(name, price)
              VALUES(?,?) '''
        cur.executemany(sql, [('Menu A', 2000), ('Menu B', 4000), ('Menu C', 8000), ('Menu D', 16000)])
        self.commit()

        self.close()
        print("Menu seeding succesfully")