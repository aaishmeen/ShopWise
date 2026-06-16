import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            category VARCHAR(100),
            price NUMERIC(10,2)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id SERIAL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            search_date DATE NOT NULL,
            search_time TIME NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id SERIAL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            price NUMERIC(10,2) NOT NULL,
            recorded_date DATE DEFAULT CURRENT_DATE,
            recorded_time TIME DEFAULT CURRENT_TIME
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()

def get_connection():

    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def add_favorite(title, category, price):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO favorites
            (title, category, price)
            VALUES (%s, %s, %s)""",
            (title, category, price)
        )

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def get_favorites():

    conn=None
    cursor = None

    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM favorites""")

        return cursor.fetchall()
    
    except Exception as e:
        print(f"Database Error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

    

def delete_favorite(favorite_id):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM favorites
            WHERE id = %s""",
            (favorite_id,)
        )

        deleted_rows = cursor.rowcount

        conn.commit()

        return deleted_rows

    except Exception as e:
        print(f"Database Error: {e}")
        return 0

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def add_search_history(product_name, search_date, search_time):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO search_history
            (product_name, search_date, search_time)
            VALUES (%s, %s, %s)""",
            (product_name, search_date, search_time)
        )

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def get_search_history():

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM search_history""")

        return cursor.fetchall()

    except Exception as e:
        print(f"Database Error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def delete_search_history(history_id):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM search_history
            WHERE id = %s """,
            (history_id,)
        )

        deleted_rows = cursor.rowcount

        conn.commit()

        return deleted_rows

    except Exception as e:
        print(f"Database Error: {e}")
        return 0

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def clear_search_history():

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM search_history""")

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def get_price_history():

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM price_history""")

        return cursor.fetchall()

    except Exception as e:
        print(f"Database Error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def get_product_prices(product_name):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT price
            FROM price_history
            WHERE product_name = %s""",
            (product_name,)
        )

        return cursor.fetchall()

    except Exception as e:
        print(f"Database Error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def add_price_record(product_name, price):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO price_history
            (product_name, price)
            VALUES (%s, %s)""",
            (product_name, price)
        )

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
