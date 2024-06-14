import sqlite3
import json

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_tables_table()

    def create_tables_table(self):
        with self.connection:
            self.connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS tables (
                    title TEXT,
                    num_rows INTEGER,
                    num_cols INTEGER,
                    column_headings TEXT,
                    data TEXT
                )
                '''
            )

    def save_to_database(self, table):
        try:
            with self.connection:
                self.connection.execute(
                    '''
                    INSERT INTO tables (title, num_rows, num_cols, column_headings, data) 
                    VALUES (?, ?, ?, ?, ?)
                    ''',
                    (table.title, table.num_rows, table.num_cols, json.dumps(table.column_headings), json.dumps(table.data))
                )
                self.connection.commit()  # Commit transaction
                print(f"Table '{table.title}' saved to database successfully.")
        except Exception as e:
            print(f"An error occurred while saving table '{table.title}' to database: {e}")

    def fetch_from_database(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tables')
        return cursor.fetchall()

    def delete_from_database(self, table):
        with self.connection:
            self.connection.execute(
                '''
                DELETE FROM tables WHERE title = ?
                ''',
                (table.title,)
            )
