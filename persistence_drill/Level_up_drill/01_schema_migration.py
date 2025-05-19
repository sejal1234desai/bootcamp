# 01_schema_migration.py
import psycopg2

# Original table setup (Run only once)
def setup_initial_schema():
    conn = psycopg2.connect("dbname=levelup_db user=postgres password=newpassword")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);")
    conn.commit()
    cur.close()
    conn.close()

# Apply migration safely
def apply_migration():
    conn = psycopg2.connect("dbname=levelup_db user=postgres password=newpassword")
    cur = conn.cursor()
    try:
        cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;")
        conn.commit()
        print("Migration applied successfully.")
    except Exception as e:
        print("Migration failed:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    setup_initial_schema()
    apply_migration()
