import datetime
import pytz
import sqlite3


class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(self.logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_user(self):
        sql = """
        CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY UNIQUE,
                data VARCHAR(255) NOT NULL,
                user_name VARCHAR(255) NOT NULL,
                first_name VARCHAR(255) NOT NULL
                );
"""
        self.execute(sql, commit=True)

    def add_user(self, id: int, user_name: str, first_name: str, data: int):
        sql = """
              INSERT INTO user(id, user_name, first_name, data) VALUES(?,?,?,?)
              """
        self.execute(sql, parameters=(id, user_name, first_name, data), commit=True)

    def select_all_user(self):
        sql = """
        SELECT * FROM user
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, user_id: int):
        sql = f"SELECT * FROM user WHERE id=?"
        return self.execute(sql, parameters=(user_id,), fetchone=True)

    def count_user(self):
        return self.execute("SELECT COUNT(*) FROM user;", fetchone=True)

    def delete_user_by_id(self, id):
        self.execute(f"DELETE FROM user WHERE id={id}", commit=True)

    def get_last_24_hours_users(self):
        tz = pytz.timezone('Asia/Tashkent')
        now = int(datetime.datetime.now(tz).timestamp())
        last_24_hours = now - 24 * 60 * 60
        sql = f"SELECT * FROM user WHERE data > {last_24_hours}"
        return self.execute(sql, fetchall=True)

    def get_last_month_users(self):
        tz = pytz.timezone('Asia/Tashkent')
        now = datetime.datetime.now(tz)
        last_month = now - datetime.timedelta(days=30)

        sql = f"SELECT * FROM user WHERE data >= {int(last_month.timestamp())} AND data <= {int(now.timestamp())}"
        return self.execute(sql, fetchall=True)

    def logger(self, statement):
        print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
