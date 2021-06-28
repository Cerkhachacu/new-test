from app.Config import Connect

class InvoiceDetaileMigration:
    def instance_method(self='migrate'):
        print("Migrating invoice")
        conn = Connect.instance_method()
        print("Opened database successfully")

        conn.execute('''
            CREATE TABLE IF NOT EXISTS invoice_detail
                (id INTEGER     PRIMARY KEY,
                menu_id       INT    NOT NULL,
                invoice_id         INT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
            );''')
        conn.execute('''
            CREATE TRIGGER trigger_invoice_detail_updated_at AFTER UPDATE ON invoice_detail
            BEGIN
                UPDATE invoice_detail SET updated_at = DATETIME('now', 'localtime') WHERE rowid == NEW.rowid;
            END;''')
        print("Table created successfully")

        conn.close()
        print("Invoice migrate succesfully")