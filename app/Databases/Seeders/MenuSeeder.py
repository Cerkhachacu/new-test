class MenuSeeder:
    def instance_method(self='seed'):
        print("Seeding menu")

        cur = self.cursor()

        sql = ''' INSERT INTO menus(name, price)
              VALUES(?,?) '''
        cur.executemany(sql, [('Menu A', 16000), ('Menu B', 32000), ('Menu C', 64000), ('Menu D', 128000)])
        self.commit()

        self.close()
        print("Menu seeding succesfully")