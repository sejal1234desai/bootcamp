# update_data.py
import sqlite3

def update_data(id, new_price):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE products SET price = ? WHERE id = ?
        ''', (new_price, id))
        conn.commit()
        print("Product updated successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error updating data: {e}")

if __name__ == "__main__":
    update_data(1, 1600.00)  # Update the price of the product with ID 1
