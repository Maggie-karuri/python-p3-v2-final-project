import csv
import json
from tables import Table
from database import Database

class TableManager:
    def __init__(self):
        self.tables = []
        self.database = Database("Table_db.db")
        self.load_tables_from_database()

    def create_table(self):
        table = Table()
        table.prompt_table_info()
        self.tables.append(table)
        self.database.save_to_database(table)
    def edit_table(self):
        table_idx = self.select_table("edit")
        if table_idx is not None:
            self.display_table_details(table_idx)
            self.database.save_to_database(self.tables[table_idx]) 

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
            print(f"\n========================================")
            print(f"Table: {table.title}\n")

            # Calculate maximum length for each column
            max_lengths = [max(len(str(row[i])) for row in table.data) for i in range(len(table.column_headings))]

            # Print column headings
            heading_row = " | ".join(column.center(max_lengths[i]) for i, column in enumerate(table.column_headings))
            print(heading_row)

            # Print separator line
            separator = " | ".join("-" * max_lengths[i] for i in range(len(table.column_headings)))
            print(separator)

            # Print table data
            for row in table.data:
                data_row = " | ".join(str(cell).center(max_lengths[i]) for i, cell in enumerate(row))
                print(data_row)

            print(f"========================================")
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
        for data_tuple in tables_data:
            try:
                title = data_tuple[0]
                num_rows = data_tuple[1]
                num_cols = data_tuple[2]
                column_headings_str = data_tuple[3]
                data_str = data_tuple[4]
            
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

    def find_longest_table_data_length(self, table):
        max_lengths = [len(str(column)) for column in table.column_headings]

        for row in table.data:
            for i, cell in enumerate(row):
                max_lengths[i] = max(max_lengths[i], len(str(cell)))

        return max_lengths
    def export_table_to_csv(self, table_idx):
        try:
            table = self.tables[table_idx]
            filename = f"{table.title.replace(' ', '_')}.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                
                # Find the max length of data for alignment
                max_data_length = max(len(str(cell)) for row in table.data for cell in row)
                max_header_length = max(len(header) for header in table.column_headings)
                column_width = max(max_data_length, max_header_length)

                # Write headers
                writer.writerow([header.ljust(column_width) for header in table.column_headings])
                writer.writerow(['=' * column_width] * len(table.column_headings))
                
                # Write data rows
                for row in table.data:
                    formatted_row = [str(cell).ljust(column_width) for cell in row]
                    writer.writerow(formatted_row)
                
            print(f"Table '{table.title}' has been exported to {filename}")
        except IndexError:
            print("Invalid table index.")
        except Exception as e:
            print(f"An error occurred while exporting the table: {e}")