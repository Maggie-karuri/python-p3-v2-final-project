import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

def execute_query(query, params=None):
    global CONN, CURSOR
    if params:
        CURSOR.execute(query, params)
    else:
        CURSOR.execute(query)
    CONN.commit()
    return CURSOR.fetchall()