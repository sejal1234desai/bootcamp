import sqlite3

# Connect to the database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Create the products table with the quantity column
def create_products_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL)''')
    conn.commit()

# Create the inventory_log table
def create_inventory_log_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory_log (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_id INTEGER,
                        change INTEGER,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(product_id) REFERENCES products(id))''')
    conn.commit()

# Insert a product into the products table
def insert_product(name, price, quantity):
    cursor.execute('''INSERT INTO products (name, price, quantity)
                      VALUES (?, ?, ?)''', (name, price, quantity))
    conn.commit()

# Log inventory changes
def log_inventory_change(product_id, change):
    cursor.execute('''INSERT INTO inventory_log (product_id, change)
                      VALUES (?, ?)''', (product_id, change))
    conn.commit()

# Update product quantity in the products table
def update_product_quantity(product_id, quantity_change):
    cursor.execute('''UPDATE products
                      SET quantity = quantity + ?
                      WHERE id = ?''', (quantity_change, product_id))
    conn.commit()

# Simulate inventory update and log
def handle_inventory_transaction():
    try:
        # Start a transaction
        conn.execute('BEGIN TRANSACTION')

        # Insert new products
        insert_product("Headphones", 1200.0, 10)  # Insert a product
        insert_product("Tablet", 499.99, 2)  # Insert a product

        # Fetch the product id of the inserted product
        cursor.execute("SELECT id FROM products WHERE name = 'Headphones'")
        product_id = cursor.fetchone()[0]

        # Update the product quantity
        update_product_quantity(product_id, -2)  # Decrease quantity of 'Headphones' by 2

        # Log the inventory change
        log_inventory_change(product_id, -2)

        # Commit the transaction
        conn.commit()
        print("Inventory transaction completed successfully.")

    except sqlite3.Error as e:
        # Rollback in case of an error
        conn.rollback()
        print(f"An error occurred: {e}")

# Function to setup the tables and perform transaction
def setup_inventory_tables():
    create_products_table()
    create_inventory_log_table()

# Run the transaction script
setup_inventory_tables()
handle_inventory_transaction()

# Close the database connection
conn.close()
