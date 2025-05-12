import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.db_name = db_name

    def batch_insert_products(self, products):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("BEGIN")  # Start transaction
            cursor.executemany("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", products)
            conn.commit()
            print(f"{len(products)} products inserted successfully in a batch.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Batch insert failed. Rolled back transaction.")
            print("Error:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    p = Product()
    batch = [
        ("Tablet", 499.99, 2),
        ("Router", 129.50, 3),
        ("Bluetooth Speaker", 89.99, 3)
    ]
    p.batch_insert_products(batch)
