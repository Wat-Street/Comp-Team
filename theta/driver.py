# driver to connect to SQL server and store csv data per exchange and per asset in ExchangeData folder 
from sql_connection import SQLConnection
from utility import query, segregateExchangeAndAssets

if __name__ == "__main__":
    SQLObject = SQLConnection()
    connection = SQLObject.create_connection()
    cursor = connection.cursor()

    # connection successful (add operations to read data here)