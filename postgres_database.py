import psycopg

def get_connection():

    return psycopg.connect(
        host="localhost",
        dbname="shopwise",
        user="postgres",
        password="aaishxxpostgres"
    )

