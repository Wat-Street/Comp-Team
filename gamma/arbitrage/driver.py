# driver to connect to SQL server and store csv data per exchange and per asset in ExchangeData folder
from sql_connection import SQLConnection
from getData import Database

if __name__ == "__main__":
    SQLObject = SQLConnection()
    connection = SQLObject.create_connection()
    cursor = connection.cursor()
    database = Database(cursor)
    print(database.getTables())


    # connection successful (add operations to read data here)
