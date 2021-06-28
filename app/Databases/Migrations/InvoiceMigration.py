from app.Config import Connect

class InvoiceMigration:
    def instance_method(self='migrate'):
        print("Migrating invoice")
        conn = Connect.instance_method()
        print("Opened database successfully")

        conn.execute('''
            CREATE TABLE IF NOT EXISTS invoices
                (id INTEGER     PRIMARY KEY,
                name           CHAR(50)    NOT NULL,
                total         INT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
            );''')
        conn.execute('''
            CREATE TRIGGER trigger_invoices_updated_at AFTER UPDATE ON invoices
            BEGIN
                UPDATE invoices SET updated_at = DATETIME('now', 'localtime') WHERE rowid == NEW.rowid;
            END;''')

        print("Table created successfully")

        conn.close()
        print("Invoice migrate succesfully")