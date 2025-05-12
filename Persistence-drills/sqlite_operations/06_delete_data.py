# delete_data.py
import sqlite3

def delete_data(id):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM products WHERE id = ?
        ''', (id,))
        conn.commit()
        print("Product deleted successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")

if __name__ == "__main__":
    delete_data(1)  # Delete product with ID 1
