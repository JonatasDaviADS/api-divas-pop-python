import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='universo_pop',
        use_pure=True
    )
