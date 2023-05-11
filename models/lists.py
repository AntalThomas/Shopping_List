from db.db import sql

def all_lists():
    return sql('SELECT * FROM lists ORDER BY id')

def create_list(name):
    sql('INSERT INTO lists(name) VALUES (%s) RETURNING *', [name])

def delete_list(id):
    sql('DELETE FROM lists WHERE id=%s RETURNING *', [id])