class InvoiceMigration:
    def instance_method(self):
        print("Migrating invoice")
        
        self.execute('''
            CREATE TABLE IF NOT EXISTS invoices
                (id INTEGER     PRIMARY KEY,
                total         INT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
            );''')
        self.execute('''
            CREATE TRIGGER trigger_invoices_updated_at AFTER UPDATE ON invoices
            BEGIN
                UPDATE invoices SET updated_at = DATETIME('now', 'localtime') WHERE rowid == NEW.rowid;
            END;''')

        print("Table created successfully")

        print("Invoice migrate succesfully")