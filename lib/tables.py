import json

class Table:
    def __init__(self, title=None, num_rows=None, num_cols=None, data=None, column_headings=None):
        self.title = title
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = data if data else []
        self.column_headings = column_headings if column_headings else []

    def prompt_table_info(self):
        self.title = input("Enter table title: ")
        self.num_rows = int(input("Enter number of rows: "))
        self.num_cols = int(input("Enter number of columns: "))
        self.column_headings = []
        for i in range(self.num_cols):
            heading = input(f"Enter heading for column {i + 1}: ")
            self.column_headings.append(heading)
        
        print("Enter table data row by row in the format '[\"a\", \"b\", \"c\"]':")
        for _ in range(self.num_rows):
            row_data = input("Enter data for row: ")
            try:
                row = json.loads(row_data)
                if len(row) != self.num_cols:
                    raise ValueError("Incorrect number of columns")
                self.data.append(row)
            except json.JSONDecodeError:
                print("Error processing row data: Invalid JSON format")
            except ValueError as e:
                print(f"Error processing row data: {e}")

