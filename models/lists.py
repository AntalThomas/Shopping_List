from db.db import sql

def all_lists():
    return sql('SELECT * FROM lists ORDER BY id')