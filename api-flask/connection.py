import sqlite3
import sys

class Connection():
    __DATABASE = 'database.db'
    __connection = None
    __cursor = None

    @classmethod
    def getConnection(cls):

        if cls.__connection is None:
            try:
               cls.__connection = sqlite3.connect(database = cls.__DATABASE)
               print(f'Connected to: {cls.__connection}')
               return cls.__connection
            except Exception as error:
                print(f'Error connecting to database: {error}')
                sys.exit()

        else:
            return cls.__connection

    @classmethod
    def getCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.getConnection().cursor()
                print(f'Cursor openned: {cls.__cursor}')
                return cls.__cursor
            except Exception as error:
                print(f'Error getting cursor: {error}')
                sys.exit()
        else:
            return cls.__cursor

    @classmethod
    def close(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
                print(f'Cursor closed')
            except Exception as error:
                print(f'Error closing cursor: {error}')

        if cls.__connection is not None:
            try:
                cls.__connection.close()
                print(f'Connection closed')
            except Exception as error:
                print(f'Error closing connection: {error}')


