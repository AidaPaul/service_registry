import sqlite3


class Registry(object):
    def __init__(self):
        self.conn = sqlite3.connect('service_registry.db')
        self.conn.isolation_level = None
        self.conn.row_factory = sqlite3.Row

    def reset(self):
        self.conn.execute('DROP TABLE IF EXISTS services')
        self.conn.execute('CREATE TABLE IF NOT EXISTS `services` (id INTEGER PRIMARY KEY AUTOINCREMENT, service TEXT, version TEXT)')

    def add_service(self, service, version):
        rows = self.conn.execute("INSERT INTO services (service, version) VALUES (?, ?)", [service, version]).rowcount
        return "created" if rows == 1 else "error"

    def remove_service(self, service_id):
        rows = self.conn.execute("DELETE FROM services WHERE id = ?", [service_id]).rowcount
        return "removed" if rows == 1 else "error"

    def update_service_version(self, service_id, version):
        rows = self.conn.execute("UPDATE services SET version = ? WHERE id = ?", [version, service_id]).rowcount
        return "changed" if rows == 1 else "error"

