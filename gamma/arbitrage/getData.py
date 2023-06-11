from utility.query import query

class Database:
    def __init__(self, cursor):
        self.tables = {}
        self.cursor = cursor
        self.getTables()

    def getTables(self):
        tables = query("SHOW TABLES", self.cursor)[0]
        for table in tables:
            self.tables[table] = Table(table, self.cursor)
        return self.tables.keys()



class Table:
    def __init__(self, table_name, cursor):
        self.table_name = table_name
        self.cursor = cursor
        self.cols = []
        self.getCols()

    def getCols(self):
        self.cols = [r[0] for r in query(f"SHOW COLUMNS FROM {self.table_name}", self.cursor)]
        print(self.cols)
