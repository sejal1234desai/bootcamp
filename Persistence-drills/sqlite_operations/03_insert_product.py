# insert_product.py
import sqlite3

def insert_product(name, price):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, price) VALUES (?, ?)
        ''', (name, price))
        conn.commit()
        print("Product inserted successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error inserting product: {e}")

if __name__ == "__main__":
    insert_product('Laptop', 1500.00)  # Example product
