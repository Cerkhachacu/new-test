class MenuMigration:
    def instance_method(self):
        print("Migrating menu")
        
        self.execute('''
            CREATE TABLE IF NOT EXISTS menus
                (id     INTEGER     PRIMARY KEY,
                name    CHAR(50) NOT NULL,
                price   INT     NOT NULL,
                created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
            )''')
        self.execute('''
            CREATE TRIGGER trigger_menus_updated_at AFTER UPDATE ON menus
            BEGIN
                UPDATE menus SET updated_at = DATETIME('now', 'localtime') WHERE rowid == NEW.rowid;
            END;''')
        print("Table created successfully")

        print("Menu migrate succesfully")