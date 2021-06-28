import sqlite3
from sqlite3.dbapi2 import Error

class Connect:
    def instance_method(self=''):
        conn = None
        try:
            conn = sqlite3.connect('app/Databases/kelompok_tiga.db')
        except Error as e:
            print(e)

        return conn