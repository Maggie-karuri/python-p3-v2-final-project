import csv
import json
from tables import Table
from database import Database

class TableManager:
    def __init__(self):
        self.tables = []
        self.database = Database("Table_db")
        self.load_tables_from_database()

    def create_table(self):
        table = Table()
        table.prompt_table_info()
        self.tables.append(table)
        self.save_to_database(table)

    def display_tables(self):
        if not self.tables:
            print("No tables created yet.")
        else:
            print("\nTables:")
            for idx, table in enumerate(self.tables, start=1):
                print(f"{idx}. {table.title}")

    def select_table(self, action="view"):
        if not self.tables:
            print("No tables created yet.")
            return None
        self.display_tables()
        try:
            choice = int(input(f"Enter the index of the table to {action}: "))
            table_idx = choice - 1
            if 0 <= table_idx < len(self.tables):
                return table_idx
            else:
                print("Invalid table index.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid table index.")
            return None

    def display_table_details(self, table_idx):
        try:
            table = self.tables[table_idx]
            table.display_table()
        except IndexError:
            print("Invalid table index.")

    def edit_table(self, table_idx):
        try:
            table = self.tables[table_idx]
            print(f"Editing Table {table_idx + 1}: {table.title}")
            table.prompt_table_info()
            self.tables[table_idx] = table
            self.save_to_database(table)
        except IndexError:
            print("Invalid table index.")

    def delete_table(self, table_idx):
        try:
            deleted_table = self.tables.pop(table_idx)
            print(f"Table {table_idx + 1} '{deleted_table.title}' deleted successfully.")
            self.database.delete_from_database(deleted_table)
        except IndexError:
            print("Invalid table index.")
    def load_tables_from_database(self):
        self.tables.clear()
        tables_data = self.database.fetch_from_database()
        for data in tables_data:
            title, num_rows, num_cols, column_headings_str, data_str = data
            try:
                if column_headings_str.strip() == "" or data_str.strip() == "":
                    raise ValueError("Empty JSON data")

                # Log or print the JSON strings for debugging
                print(f"Column Headings JSON: {column_headings_str}")
                print(f"Data JSON: {data_str}")

                column_headings = json.loads(column_headings_str)
                data = json.loads(data_str)

                if not isinstance(column_headings, list) or not all(isinstance(item, str) for item in column_headings):
                    raise ValueError("Invalid column headings format")
                if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
                    raise ValueError("Invalid data format")

                table = Table(title, num_rows, num_cols, data, column_headings)
                self.tables.append(table)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for table '{title}'. Skipping this table.")
                print(f"Error: {e}")
                continue
            except ValueError as ve:
                print(f"Error loading table '{title}' from database: {ve}")
                continue

    def save_to_database(self, table):
        try:
            # Serialize column_headings and data to JSON strings
            column_headings_str = json.dumps(table.column_headings)
            data_str = json.dumps(table.data)

            # Save to database (simulate database saving operation)
            table_data = (table.title, table.num_rows, table.num_cols, column_headings_str, data_str)
            self.database.save_to_database(table_data)
        except Exception as e:
            print(f"An error occurred while saving table '{table.title}' to database: {e}")

    def export_table_to_csv(self, table_idx):
        try:
            table = self.tables[table_idx]
            filename = f"{table.title.replace(' ', '_')}.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(table.column_headings)
                writer.writerow(['-' * 15 for _ in range(len(table.column_headings))])

                for row in table.data:
                    writer.writerow(row)
            print(f"Table '{table.title}' has been exported to {filename}")
        except IndexError:
            print("Invalid table index.")
        except Exception as e:
            print(f"An error occurred while exporting the table: {e}")
