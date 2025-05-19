import sqlite3


def setup_order_tables():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            status TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_details (
            detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_name TEXT,
            quantity INTEGER,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    """)

    # Insert a sample order for the update test
    cursor.execute("INSERT INTO orders (customer_name, status) VALUES (?, ?)", ("Ritika Sharma", "pending"))
    order_id = cursor.lastrowid
    cursor.execute("INSERT INTO order_details (order_id, product_name, quantity) VALUES (?, ?, ?)",
                   (order_id, "Router", 1))
    conn.commit()
    conn.close()
    return order_id


def update_order_and_details(order_id):
    try:
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        cursor.execute("BEGIN")

        cursor.execute("UPDATE orders SET status = ? WHERE order_id = ?", ("completed", order_id))
        cursor.execute("UPDATE order_details SET quantity = quantity + 1 WHERE order_id = ?", (order_id,))

        conn.commit()
        print("Order and details updated successfully in a single transaction.")
    except sqlite3.Error as e:
        conn.rollback()
        print("Transaction failed. Rolled back.")
        print("Error:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    order_id = setup_order_tables()
    update_order_and_details(order_id)
