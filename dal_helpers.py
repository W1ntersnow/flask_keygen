import sqlite3
import config


class DBBaseCommands:
    connection = None

    @staticmethod
    def create_default_conn():
        return sqlite3.connect(config.DATABASE_NAME)

    def define_connection(self):
        if not isinstance(self.connection, sqlite3.Connection):
            self.connection = self.create_default_conn()
        return self.connection

    def execute_query(self, query, *args, commit=False):
        connection = self.define_connection()
        query = query.format(*args) if args else query
        rows = connection.execute(query)
        if commit:
            connection.commit()
        return rows.fetchall()

    def close_connection(self):
        if isinstance(self.connection, sqlite3.Connection):
            self.connection.close()
