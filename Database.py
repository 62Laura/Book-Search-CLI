import sqlite3

DB_NAME = "books.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Drop the table if it already exists (CAUTION: This deletes all saved favorites)
    cursor.execute("DROP TABLE IF EXISTS favorites")

    # Recreate the table with the correct columns
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

# Run this once to fix the issue
init_db()
print("Database initialized successfully!")
