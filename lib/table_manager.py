# lib/table_manager.py

from tables import Table
from database import Database

class TableManager:
    def __init__(self):
        self.tables = []
        self.database = Database("example_db")  # Replace "example_db" with your actual database name

    def create_table(self):
        table = Table()
        table.prompt_table_info()
        self.tables.append(table)
        self.database.save_to_database(table)  # Save table to database

    def display_tables(self):
        if not self.tables:
            print("No tables created yet.")
        else:
            while True:
                print("\nTables:")
                for idx, table in enumerate(self.tables, start=1):
                    print(f"{idx}. {table.title}")
                print("0. Return to main menu")

                try:
                    choice = int(input("Enter the index of the table to view details: "))
                    if choice == 0:
                        return  # Return to main menu
                    table_idx = choice - 1
                    if 0 <= table_idx < len(self.tables):
                        self.display_table_details(table_idx)
                        input("Press Enter to return to main menu...")
                    else:
                        print("Invalid table index.")
                except ValueError:
                    print("Invalid input. Please enter a valid table index.")

    def display_table_details(self, table_idx):
        try:
            table = self.tables[table_idx]
            print(f"\nTable {table_idx + 1}: {table.title}")
            print("   Columns: " + ", ".join(table.column_headings))
            print("   Data:")
            heading_row = "     " + " | ".join(column.center(15) for column in table.column_headings)
            print(heading_row)
            print("     " + "-" * len(heading_row))
            for row in table.data:
                data_row = "     " + " | ".join(str(cell).center(15) for cell in row)
                print(data_row)
        except IndexError:
            print("Invalid table index.")
        
        # Implement editing logic for the table (e.g., modify title, add/remove rows, etc.)
        print(f"Editing Table {table_idx + 1}: {table.title}")
        table.prompt_table_info()
        self.database.save_to_database(table)  # Save updated table to database

    def delete_table(self, table_idx):
        try:
            deleted_table = self.tables.pop(table_idx)
            print(f"Table {table_idx + 1} '{deleted_table.title}' deleted successfully.")
            self.database.delete_from_database(deleted_table)  # Delete table from database
        except IndexError:
            print("Invalid table index.")

    def load_tables_from_database(self):
        tables_data = self.database.fetch_from_database()
        for data in tables_data:
            title, num_rows, num_cols, column_headings_str, data_str = data
            column_headings = column_headings_str.split(",")
            data = eval(data_str)  # Note: This assumes safe evaluation, ensure data safety
            table = Table(title, num_rows, num_cols, data, column_headings)
            self.tables.append(table)
