from datetime import datetime
import sqlite3
import urllib.request

DB = "hunter.db"

SOURCES = [
    {
        "name": "Immobiliare.it",
        "url": "https://www.immobiliare.it/vendita-case/roma/da-privati/"
    },
    {
        "name": "Casa.it",
        "url": "https://www.casa.it/vendita/residenziale/roma/"
    }
]


def init_database():
    conn = sqlite3.connect(DB)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            url TEXT,
            last_check TEXT
        )
    """)

    conn.commit()
    conn.close()


def check_source(source):
    print(f"Controllo: {source['name']}")

    try:
        request = urllib.request.Request(
            source["url"],
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
            print(f"Risposta HTTP: {status}")

            return True

    except Exception as error:
        print(f"Fonte non accessibile: {error}")
        return False


def main():
    print("=" * 50)
    print("HUNTER — TEST RACCOLTA")
    print("=" * 50)

    init_database()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Avvio: {now}")

    for source in SOURCES:
        check_source(source)

    print("=" * 50)
    print("TEST TERMINATO")
    print("=" * 50)


if __name__ == "__main__":
    main()
