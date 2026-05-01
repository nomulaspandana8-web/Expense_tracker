import sqlite3
DB_NAME = "expenses.db"
def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,amount REAL,category TEXT)""")
    conn.commit()
    conn.close()