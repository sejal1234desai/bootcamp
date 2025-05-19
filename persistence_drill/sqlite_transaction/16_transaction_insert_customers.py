import sqlite3

def create_customers_table():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_customers_in_transaction(customers):
    try:
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        cursor.execute("BEGIN")  # Begin transaction

        cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers)

        conn.commit()
        print(f"{len(customers)} customers inserted successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        print("Transaction failed. Rolled back.")
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    create_customers_table()

    customers = [
        ("Aarav Patil", "aarav@example.com"),
        ("Isha More", "isha@example.com"),
        ("Siddharth Kale", "sid@example.com")
    ]
    insert_customers_in_transaction(customers)
