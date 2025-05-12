import sqlite3
import csv

def export_products_to_csv():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    with open("products_export.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'Price', 'Category ID'])
        writer.writerows(products)

    conn.close()
    print("Exported products to products_export.csv")

if __name__ == "__main__":
    export_products_to_csv()
