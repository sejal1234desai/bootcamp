# create_db.py
import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('store.db')
        print("Database created successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    create_database()
