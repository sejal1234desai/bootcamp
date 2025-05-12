# create_table.py
import sqlite3

def create_table():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            );
        ''')
        conn.commit()
        print("Table created successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    create_table()
