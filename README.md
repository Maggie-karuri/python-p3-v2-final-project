# Table Manager Application

- This project is a simple Python application that helps you manage tables, add data, edit them, and even export them to CSV files. It's built using Python's basic features and stores data in a local SQLite database.
 - Ideal for scenarios where users need to input, manage, and analyze structured data efficiently.

## Features

- **Create Table**: You can create new tables by defining columns and entering data.
- **Edit Table**: Modify existing tables, like changing titles or updating data.
- **Delete Table**: Remove tables you no longer need.
- **Display Tables**: See all the tables you've created.
- **Export Table to CSV**: Save your tables as CSV files for sharing or backup.

## Components

### `lib/table_manager.py`

This file has the `TableManager` class, which does most of the work:
- Creates, edits, and deletes tables.
- Displays tables and their contents.
- Exports tables to CSV files.

### `lib/tables.py`

Defines the `Table` class, which represents a table:
- Stores table details like title, columns, and data.
- Provides methods to change table properties and validate data.

### `lib/database.py`

Manages the database (`Table_db.db`) using SQLite:
- Saves tables into the database.
- Retrieves tables from the database.
- Deletes tables when you don't need them anymore.

### `lib/cli.py`

This is where you interact with the application:
- You'll see menus with options to create, edit, delete, display, and export tables.
- Choose options by entering numbers.

## Installation

1. **Clone the Project**: Copy the project to your computer:
git clone <repository_url>
cd <repository_directory>

markdown
Copy code

2. **Install Dependencies**: Make sure you have Python 3 installed. Install required libraries:
pip install -r requirements.txt

markdown
Copy code

3. **Start the Program**: Run the program to begin managing tables:
python lib/cli.py

markdown
Copy code

## How to Use

- Follow the prompts in the command line to perform actions like creating, editing, and exporting tables.
- Your tables are stored in `Table_db.db` in the project folder.

## Example

Here’s an example of what you can do with the Table Manager:

0. Exit the Program
1. Create a new table and add data to it.
2. Edit a table to change its title or update its data.
3. Delete an existing table from database.
4. Display all tables to see what you’ve created.
5. Export a table to a CSV file for use in other programs.