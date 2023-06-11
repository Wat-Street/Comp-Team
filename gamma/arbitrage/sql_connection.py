import os
import mysql.connector
import pandas as pd
import rollbar
from dotenv import load_dotenv

load_dotenv()

class SQLConnection:
    def __init__(self):
        self.__user = os.environ.get('USERNAME')
        self.__password = os.environ.get('PASSWORD')
        self.__host = os.environ.get('HOST')
        self.__database = os.environ.get('DATABASE')

    def create_connection(self):
        config = {
            'user': self.__user,
            'password': self.__password,
            'host': self.__host,
            'database': self.__database,
            'raise_on_warnings': True
        }
        try:
            return mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            print(err)
            rollbar.report_exc_info()
            exit()
