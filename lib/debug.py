#!/usr/bin/env python3
# lib/debug.py

from models import CONN, CURSOR  # Import CONN and CURSOR from models/__init__.py
import ipdb

def debug_database():
    ipdb.set_trace()  # Set a breakpoint for debugging
    
    try:
        # Example: Query the database
        CURSOR.execute("SELECT * FROM your_table")
        rows = CURSOR.fetchall()
        for row in rows:
            print(row)
        
        # Example: Modify database data
        #CURSOR.execute("UPDATE your_table SET column = value WHERE condition")
        #CONN.commit()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_database()
