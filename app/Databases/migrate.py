from app.Databases.Seeders.MenuSeeder import MenuSeeder
from app.Databases.Migrations.MenuMigration import MenuMigration
from app.Databases.Migrations.InvoiceMigration import InvoiceMigration
from app.Databases.Migrations.InvoiceDetailMigration import InvoiceDetaileMigration

class migrate:
    def migrate_and_seed_all(self):
        MenuMigration.instance_method()
        InvoiceMigration.instance_method()
        InvoiceDetaileMigration.instance_method()
        MenuSeeder.instance_method()
        