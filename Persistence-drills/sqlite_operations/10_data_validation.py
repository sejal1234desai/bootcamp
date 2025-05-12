# data_validation.py
import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def validate_data(self, name, price):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string!")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number!")

    def add_product(self, name, price):
        try:
            self.validate_data(name, price)
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
            conn.commit()
            conn.close()
            print(f"Product '{name}' added successfully!")
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
        except ValueError as e:
            print(f"Data validation error: {e}")

# Example usage
if __name__ == "__main__":
    product = Product()
    product.add_product('Laptop', 999.99)  # Valid data
    product.add_product('Tablet', -150)  # Invalid data
