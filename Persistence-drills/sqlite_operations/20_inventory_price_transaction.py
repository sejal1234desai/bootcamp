import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Ensure the tables are set up correctly
def setup_tables():
    # Create the products table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')

    # Create the inventory_log table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        change INTEGER NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products (id)
    )
    ''')

    # Insert sample data if needed (You can skip this step if your data is already populated)
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES ('Laptop', 1500.0, 5)")
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES ('Smartphone', 799.99, 10)")
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES ('Smartwatch', 299.99, 2)")
    conn.commit()

# Method to update inventory and log the transaction
def update_inventory_and_log(product_id, price_change, quantity_change):
    try:
        # Start a transaction
        conn.execute("BEGIN TRANSACTION")

        # Update the product's price and quantity
        cursor.execute('''
        UPDATE products
        SET price = price + ?, quantity = quantity + ?
        WHERE id = ?
        ''', (price_change, quantity_change, product_id))

        # Log the change in inventory_log
        cursor.execute('''
        INSERT INTO inventory_log (product_id, change, timestamp)
        VALUES (?, ?, ?)
        ''', (product_id, quantity_change, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        # Commit the transaction
        conn.commit()
        print("Transaction committed successfully.")

    except Exception as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        print("An error occurred, transaction rolled back:", e)

# Example of updating inventory (decrease quantity by 2 and price increase by 100)
def update_example():
    # Update the inventory of 'Smartphone' (product_id 2) - decrease 2 in quantity and increase 100 in price
    update_inventory_and_log(2, 100, -2)

# Main execution
if __name__ == "__main__":
    setup_tables()  # Set up tables and data if needed
    update_example()  # Perform the example update
