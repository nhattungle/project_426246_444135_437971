import sqlite3

#########################################################
# Connection
class Connection:
    @staticmethod
    def getConnection():
        conn = sqlite3.connect('database.db', timeout=10)
        return conn
    
    @staticmethod
    def getCursor():
        conn = sqlite3.connect('database.db', timeout=10)
        c = conn.cursor()
        return c