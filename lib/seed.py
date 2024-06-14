# lib/seed.py

import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='seed.log'  # Log file to capture logs
)

def create_tables(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id)
            )
        """)
        conn.commit()
        logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")
        raise  # Re-raise the exception for further handling

def seed_database():
    dbname = 'company.db'
    conn = sqlite3.connect(dbname)
    
    try:
        create_tables(conn)  # Ensure tables are created
        
        # Insert sample data
        cursor = conn.cursor()
        cursor.execute("INSERT INTO departments (name) VALUES ('HR')")
        cursor.execute("INSERT INTO departments (name) VALUES ('IT')")
        cursor.execute("INSERT INTO departments (name) VALUES ('Finance')")

        cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Alice', 1)")
        cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Bob', 2)")
        cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Charlie', 3)")

        conn.commit()
        logging.info("Sample data inserted successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error inserting data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    try:
        seed_database()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
