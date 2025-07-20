import sqlite3



conn = sqlite3.connect('superprof_data.db') 
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    title TEXT,
    price TEXT,
    profile_url TEXT
)
""")
conn.commit()


