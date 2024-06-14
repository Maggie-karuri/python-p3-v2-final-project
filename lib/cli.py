# lib/cli.py
from table_manager import TableManager
from helpers import exit_program

def main():
    table_manager = TableManager()
    table_manager.load_tables_from_database()  # Load tables from database on application start
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            table_manager.create_table()
        elif choice == "2":
            edit_table_menu(table_manager)
        elif choice == "3":
            delete_table_menu(table_manager)
        elif choice == "4":
            table_manager.display_tables()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new table")
    print("2. Edit an existing table")
    print("3. Delete an existing table")
    print("4. Display all tables")
    # Add more options as needed

def edit_table_menu(table_manager):
    table_manager.display_tables()
    try:
        table_idx = int(input("Enter the index of the table to edit: ")) - 1
        table_manager.edit_table(table_idx)
    except ValueError:
        print("Invalid input. Please enter a valid table index.")

def delete_table_menu(table_manager):
    table_manager.display_tables()
    try:
        table_idx = int(input("Enter the index of the table to delete: ")) - 1
        table_manager.delete_table(table_idx)
    except ValueError:
        print("Invalid input. Please enter a valid table index.")

if __name__ == "__main__":
    main()
