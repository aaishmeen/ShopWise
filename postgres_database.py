import psycopg

def get_connection():

    return psycopg.connect(
        host="localhost",
        dbname="shopwise",
        user="postgres",
        password="aaishxxpostgres"
    )

def add_favorite(title, category, price):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO favorites
        (title, category, price)
        VALUES (%s, %s, %s)
        """,
        (title, category, price)
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_favorites():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM favorites
    """)

    favorites = cursor.fetchall()

    cursor.close()
    conn.close()

    return favorites

def delete_favorite(favorite_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM favorites
        WHERE id = %s
        """,
        (favorite_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

def add_search_history(product_name,search_date,search_time):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO search_history
                   (product_name , search_date,search_time)
                   VALUES(%s, %s, %s)""",
                   (product_name,search_date,search_time))    
    
    conn.commit()
    cursor.close()
    conn.close()

def get_search_history():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT* 
        FROM search_history""")

        history = cursor.fetchall()

        cursor.close() 
        conn.close()   

        return history

def delete_search_history(history_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM search_history
            WHERE id = %s""",
            (history_id,)
        )    

    conn.commit()
    cursor.close()
    conn.close()

def clear_search_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM search_history""")


    conn.commit()
    cursor.close()
    conn.close()

def add_price_record(product_name,price):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO price_history
        (product_name, price)
        VALUES (%s, %s)
        """,
        (product_name, price)
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_price_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM price_history""")

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history

def get_product_prices(product_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT price
        FROM price_history
        WHERE product_name = %s""",
        (product_name,)
    )

    prices = cursor.fetchall()

    cursor.close()
    conn.close()

    return prices