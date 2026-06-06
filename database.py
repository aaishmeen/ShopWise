import sqlite3

DB_NAME="shopwise.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        price REAL
    )
    """)

    conn.commit()
    conn.close()

def add_favorite(title, category, price):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO favorites
    (title, category, price)
    VALUES (?, ?, ?)
    """, (title, category, price))

    conn.commit()
    conn.close()

def get_favorites():

    conn = get_connection()
    cursor =  conn.cursor()

    cursor.execute("""
    SELECT * FROM favorites
    """)

    favorites =  cursor.fetchall()

    conn.close()

    return favorites

def delete_favorite(favorite_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM favorites
    WHERE id = ?                   
    """,(favorite_id,))
    
    conn.commit()
    conn.close()

