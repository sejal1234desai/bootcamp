# search_function.py
import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def search_product(self, name_fragment):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            query = 'SELECT * FROM products WHERE name LIKE ?'
            cursor.execute(query, ('%' + name_fragment + '%',))
            products = cursor.fetchall()
            if products:
                print(f"Products matching '{name_fragment}':")
                for product in products:
                    print(product)
            else:
                print(f"No products found matching '{name_fragment}'!")
            conn.close()
        except sqlite3.Error as e:
            print(f"Error searching for products: {e}")

# Example usage
if __name__ == "__main__":
    product = Product()
    product.search_product('Smart')  # Example of searching for products by name
