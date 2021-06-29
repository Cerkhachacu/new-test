class InvoiceDetaileMigration:
    def instance_method(self):
        print("Migrating invoice")

        self.execute('''
            CREATE TABLE IF NOT EXISTS invoice_details
                (id INTEGER     PRIMARY KEY,
                menu_id       INT    NOT NULL,
                qty           INT   NOT NULL,
                invoice_id         INT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
            );''')
        self.execute('''
            CREATE TRIGGER trigger_invoice_details_updated_at AFTER UPDATE ON invoice_details
            BEGIN
                UPDATE invoice_details SET updated_at = DATETIME('now', 'localtime') WHERE rowid == NEW.rowid;
            END;''')
        print("Table created successfully")

        print("Invoice migrate succesfully")