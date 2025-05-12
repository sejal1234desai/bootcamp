import sqlite3


def setup_categories_table():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # Create categories table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    # Add category_id to products table
    cursor.execute("""
        ALTER TABLE products ADD COLUMN category_id INTEGER
    """)

    # Insert sample categories
    categories = [('Electronics',), ('Accessories',), ('Home Appliances',)]
    cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

    # Update existing products with category_id (random assignment)
    cursor.execute("UPDATE products SET category_id = 1 WHERE name LIKE '%Laptop%'")
    cursor.execute("UPDATE products SET category_id = 1 WHERE name LIKE '%Smartphone%'")
    cursor.execute("UPDATE products SET category_id = 2 WHERE name LIKE '%Smartwatch%'")

    conn.commit()
    conn.close()
    print("Categories set up and products updated.")


def fetch_products_with_categories():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.id, p.name, p.price, c.name as category
        FROM products p
        JOIN categories c ON p.category_id = c.id
    """)

    results = cursor.fetchall()
    conn.close()

    print("Products with categories:")
    for row in results:
        print(row)


if __name__ == "__main__":
    try:
        setup_categories_table()
    except sqlite3.OperationalError as e:
        # In case category_id already exists (re-run)
        print(f"Setup skipped: {e}")

    fetch_products_with_categories()
