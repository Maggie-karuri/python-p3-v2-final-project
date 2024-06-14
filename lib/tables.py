# lib/tables.py

class Table:
    def __init__(self, title="", num_rows=0, num_cols=0, data=None, column_headings=None):
        self.title = title
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = data if data else []
        self.column_headings = column_headings if column_headings else []

    def prompt_table_info(self):
        self.title = input("Enter table title: ")
        self.num_rows = int(input("Enter number of rows: "))
        self.num_cols = int(input("Enter number of columns: "))

        # Prompt for column headings
        self.column_headings = []
        for i in range(self.num_cols):
            heading = input(f"Enter heading for column {i + 1}: ")
            self.column_headings.append(heading)

        print("Enter table data row by row in the format '[a, b, c, d], [a, b, c, d]':")
        for _ in range(self.num_rows):
            row_data = input("Enter data for row: ").strip()
            row_data = row_data[1:-1]  # Remove square brackets from the beginning and end
            row = [x.strip() for x in row_data.split(",")]
            self.data.append(row)

    def display_table(self):
        print("\n" + "=" * 40)
        print(f"Table: {self.title}\n")

        # Display table headers with custom column headings
        header_row = "|".join(self.column_headings)
        print(header_row)

        # Display table data
        for row in self.data:
            row_str = "|".join(str(cell).center(10) for cell in row)
            print(row_str)
        print("=" * 40)