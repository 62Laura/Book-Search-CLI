import sqlite3

DB_NAME = "books.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            published_year TEXT,
            subjects TEXT,
            isbn TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()
print("Database initialized successfully!")
