from datetime import datetime
import sqlite3

DB = "hunter.db"


def init_database():
    conn = sqlite3.connect(DB)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            location TEXT,
            url TEXT UNIQUE,
            source TEXT,
            first_seen TEXT,
            last_seen TEXT
        )
    """)

    conn.commit()
    conn.close()


def hunter_status():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"HUNTER ATTIVO - {now}")


if __name__ == "__main__":
    init_database()
    hunter_status()
