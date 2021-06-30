from app.Databases.migrate import migrate
from app.Config.Connect import Connect
import os
filePath = './app/Databases/kelompok_tiga.db'
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    os.remove(filePath)

conn = Connect.instance_method()

migrate.migrate_and_seed_all(conn)

conn.close()