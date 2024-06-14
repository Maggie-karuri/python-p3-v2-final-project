import sqlite3
import json

class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname + ".db")
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
        try:
            self.cursor.execute(self.create_table_sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables table: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def save_to_database(self, table):
        insert_sql = """
            INSERT INTO tables (title, num_rows, num_cols, column_headings, data)
            VALUES (?, ?, ?, ?, ?)
        """
        column_headings_str = json.dumps(table.column_headings)  # Serialize column_headings to JSON string
        data_str = json.dumps(table.data)  # Serialize data to JSON string
        try:
            self.cursor.execute(insert_sql, (table.title, table.num_rows, table.num_cols, column_headings_str, data_str))
            self.conn.commit()
            print(f"Table '{table.title}' saved to database '{self.dbname}'.")
        except sqlite3.Error as e:
            print(f"Error saving table '{table.title}' to database: {e}")

    def delete_from_database(self, table):
        delete_sql = """
            DELETE FROM tables WHERE title = ?
        """
        try:
            self.cursor.execute(delete_sql, (table.title,))
            self.conn.commit()
            print(f"Table '{table.title}' deleted from database '{self.dbname}'.")
        except sqlite3.Error as e:
            print(f"Error deleting table '{table.title}' from database: {e}")

    def fetch_from_database(self):
        fetch_sql = """
            SELECT title, num_rows, num_cols, column_headings, data FROM tables
        """
        try:
            self.cursor.execute(fetch_sql)
            tables_data = self.cursor.fetchall()
            return tables_data
        except sqlite3.Error as e:
            print(f"Error fetching tables from database: {e}")
            return []

# Example of usage:
if __name__ == "__main__":
    # Example usage of Database class
    with Database("Table_db") as db:
        tables_data = db.fetch_from_database()
        for data in tables_data:
            print(data)