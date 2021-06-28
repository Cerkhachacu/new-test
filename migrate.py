from app.Databases.migrate import migrate
from app.Config.Connect import Connect

conn = Connect.instance_method()

migrate.migrate_and_seed_all(conn)

conn.close()