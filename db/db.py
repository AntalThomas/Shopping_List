import psycopg2
import psycopg2.extras

DB_URL = "dbname=shopping_list_db"

def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL) # OPEN CONNECTION
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # CURSOR TO RUN SQL COMMANDS
    cursor.execute(query, parameters) # BEGIN TRANSACTION
    results = cursor.fetchall()
    connection.commit() # END TRANSACTION
    connection.close() # CLOSE TRANSACTION
    return results