import sqlite3

# Path to the database file
db_path = "/example.db"

# Connect to SQLite Database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query data from the COMPANIES table
cursor.execute("SELECT * FROM COMPANIES")
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(f"ID: {row[0]}, Company: {row[1]}")

# Close the connection
conn.close()
