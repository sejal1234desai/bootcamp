# read_data.py
import sqlite3

def read_data():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except sqlite3.Error as e:
        print(f"Error reading data: {e}")

if __name__ == "__main__":
    read_data()
