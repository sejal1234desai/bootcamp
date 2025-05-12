# transactions.py
import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def add_products_batch(self, products):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('BEGIN TRANSACTION')
            for name, price in products:
                cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
            conn.commit()
            conn.close()
            print(f"{len(products)} products added successfully!")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Error adding products: {e}")
        finally:
            conn.close()

# Example usage
if __name__ == "__main__":
    product = Product()
    products_to_add = [
        ('Laptop', 999.99),
        ('Tablet', 300),
        ('Smartwatch', 200)
    ]
    product.add_products_batch(products_to_add)
