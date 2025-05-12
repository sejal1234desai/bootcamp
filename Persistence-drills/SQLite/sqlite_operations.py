import sqlite3

# Directly create DB in current directory (SQLite/)
db_path = "example.db"

# Connect to SQLite DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS COMPANIES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL
)
''')

# Insert unique company records
cursor.execute("INSERT INTO COMPANIES (company_name) VALUES ('NovaCrop')")
cursor.execute("INSERT INTO COMPANIES (company_name) VALUES ('AgriSphere')")
cursor.execute("INSERT INTO COMPANIES (company_name) VALUES ('FarmIQ')")

# Commit and close
conn.commit()
conn.close()
