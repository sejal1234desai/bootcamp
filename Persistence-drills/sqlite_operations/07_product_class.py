# product_class.py
import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def add_product(self, name, price):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
            conn.commit()
            conn.close()
            print(f"Product '{name}' added successfully!")
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def list_products(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            if products:
                print("Products in the database:")
                for product in products:
                    print(product)
            else:
                print("No products found!")
            conn.close()
        except sqlite3.Error as e:
            print(f"Error listing products: {e}")

# Example usage
if __name__ == "__main__":
    product = Product()
    product.add_product('Smartphone', 799.99)  # Example of adding a product
    product.list_products()  # List all products
