import sqlite3


def setup_accounts():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    """)

    cursor.execute("DELETE FROM accounts")  # clear for rerun
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Sneha", 1000))
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Karan", 500))
    conn.commit()
    conn.close()


def transfer_funds(sender_id, receiver_id, amount):
    try:
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        cursor.execute("BEGIN")

        # Check balance
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (sender_id,))
        sender_balance = cursor.fetchone()[0]

        if sender_balance < amount:
            raise Exception("Insufficient balance")

        # Perform debit and credit
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, sender_id))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, receiver_id))

        conn.commit()
        print(f"₹{amount} transferred from account {sender_id} to {receiver_id}")
    except Exception as e:
        conn.rollback()
        print("Transaction failed. Rolled back.")
        print("Error:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    setup_accounts()
    transfer_funds(1, 2, 300)  # Sneha to Karan
