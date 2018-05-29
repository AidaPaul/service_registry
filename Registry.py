import sqlite3


class Registry(object):
    def __init__(self):
        self.conn = sqlite3.connect('service_registry.db')
        self.conn.isolation_level = None
        self.conn.row_factory = sqlite3.Row

    def reset(self):
        self.conn.execute('DROP TABLE IF EXISTS services')
        self.conn.execute('CREATE TABLE IF NOT EXISTS `services` (id INTEGER PRIMARY KEY AUTOINCREMENT, service TEXT, version TEXT)')

