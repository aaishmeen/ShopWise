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

    cursor.execute("""
CREATE TABLE IF NOT EXISTS search_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        date TEXT,
        time TEXT
        )
        """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS price_history(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_name TEXT,
                   price REAL,
                   date TEXT,
                   time TEXT)""")

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

def add_search_history(product_name,date,time):

    conn =  get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO search_history
    (product_name,date,time)
    VALUES(?,?,?)
    """,(product_name,date,time))

    conn.commit()
    conn.close()


def get_search_history():

    conn = get_connection()
    cursor =  conn.cursor()

    cursor.execute("""
    SELECT * FROM search_history""")

    history = cursor.fetchall()

    conn.close()

    return history

def delete_search_history(history_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM search_history
    WHERE id =?""",(history_id,))

    conn.commit()
    conn.close()

def clear_search_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM search_history
    """)

    conn.commit()
    conn.close()    

def add_price_record(product_name,price,date,time):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO price_history
    (product_name,price,date,time)
    VALUES(?,?,?,?)"""
    ,(product_name,price,date,time))

    conn.commit()
    conn.close()    


def get_price_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM price_history
    """)

    history = cursor.fetchall()

    conn.close()

    return history    


def get_product_prices(product_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT price
    FROM price_history
    WHERE product_name = ?
    """, (product_name,))

    prices = cursor.fetchall()

    conn.close()

    return prices