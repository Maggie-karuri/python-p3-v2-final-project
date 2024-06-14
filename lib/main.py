from lib.database import Database, TableValidator
from lib.tables import Table

def main():
    # Initialize Database and TableValidator instances
    db = Database('company')  
    table_validator = TableValidator('company')
    
    # Example usage
    table_name = 'table'
    # Validate if table exists before saving
    if table_validator.validate_table_exists(table_name):
        # Perform save operation
        table = Table()  # Assuming Table class is defined elsewhere
        table.title = 'Table'
        table.num_rows = 3
        table.num_cols = 2
        table.column_headings = ['Column 1', 'Column 2']
        table.data = [['A1', 'B1'], ['A2', 'B2'], ['A3', 'B3']]
        
        db.save_to_database(table)
    else:
        print(f"Table '{table_name}' does not exist. Cannot perform save operation.")

if __name__ == "__main__":
    main()
