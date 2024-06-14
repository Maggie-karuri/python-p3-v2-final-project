from table_manager import TableManager

def main():
    manager = TableManager()
    while True:
        print("\nPlease select an option:")
        print("0. Exit the program")
        print("1. Create a new table")
        print("2. Edit an existing table")
        print("3. Delete an existing table")
        print("4. Display tables")
        print("5. Export a table to CSV")
        
        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            manager.create_table()
        elif choice == "2":
            table_idx = manager.select_table("edit")
            if table_idx is not None:
                open_and_edit_table(manager, table_idx)
        elif choice == "3":
            table_idx = manager.select_table("delete")
            if table_idx is not None:
                manager.delete_table(table_idx)
        elif choice == "4":
            manager.display_tables()  # Only display tables here
            table_idx = input("Enter the index of the table to view: ")
            if table_idx.isdigit():
                table_idx = int(table_idx) - 1
                if 0 <= table_idx < len(manager.tables):
                    open_and_edit_table(manager, table_idx)
                else:
                    print("Invalid table index.")
            else:
                print("Invalid input. Please enter a valid table index.")
        elif choice == "5":
            table_idx = manager.select_table("export")
            if table_idx is not None:
                manager.export_table_to_csv(table_idx)
        else:
            print("Invalid choice. Please select a valid option.")

def open_and_edit_table(manager, table_idx):
    while True:
        manager.display_table_details(table_idx)
        print("\nSelect an option:")
        print("1. Edit this table")
        print("2. Return to main menu")

        choice = input("> ")

        if choice == "1":
            manager.edit_table(table_idx)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
