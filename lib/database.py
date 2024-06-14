# lib/database.py
import sqlite3  # Example using SQLite, adjust as per your database system

class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname + ".db")  # Connect to SQLite database
        self.cursor = self.conn.cursor()
        self.create_table_sql = """
            CREATE TABLE IF NOT EXISTS tables (
                title TEXT,
                num_rows INTEGER,
                num_cols INTEGER,
                column_headings TEXT,
                data TEXT
            )
        """
        self.cursor.execute(self.create_table_sql)
        self.conn.commit()

    def save_to_database(self, table):
        insert_sql = """
            INSERT INTO tables (title, num_rows, num_cols, column_headings, data)
            VALUES (?, ?, ?, ?, ?)
        """
        column_headings_str = ",".join(table.column_headings)
        data_str = ",".join([str(row) for row in table.data])
        self.cursor.execute(insert_sql, (table.title, table.num_rows, table.num_cols, column_headings_str, data_str))
        self.conn.commit()
        print(f"Table '{table.title}' saved to database '{self.dbname}'.")

    def delete_from_database(self, table):
        delete_sql = """
            DELETE FROM tables WHERE title = ?
        """
        self.cursor.execute(delete_sql, (table.title,))
        self.conn.commit()
        print(f"Table '{table.title}' deleted from database '{self.dbname}'.")

    def fetch_from_database(self):
        fetch_sql = """
            SELECT title, num_rows, num_cols, column_headings, data FROM tables
        """
        self.cursor.execute(fetch_sql)
        tables_data = self.cursor.fetchall()
        return tables_data
