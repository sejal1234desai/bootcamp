import sqlite3

db_path = "example.db"  

def update_company():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE COMPANIES
        SET company_name = 'NovaCropAI'
        WHERE id = 1
    """)
    conn.commit()
    conn.close()
    print("Updated company with ID 1.")

def delete_company():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM COMPANIES
        WHERE id = 2
    """)
    conn.commit()
    conn.close()
    print("Deleted company with ID 2.")

def select_companies():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM COMPANIES")
    rows = cursor.fetchall()
    conn.close()
    print("Current Companies in DB:")
    for row in rows:
        print(row)

# Call all three for now
update_company()
delete_company()
select_companies()
