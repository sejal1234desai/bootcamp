import sqlite3

def calculate_total_product_value():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(price) FROM products")
    total = cursor.fetchone()[0]

    conn.close()
    return total

if __name__ == "__main__":
    total_value = calculate_total_product_value()
    print(f"Total value of all products: ₹{total_value:.2f}")
