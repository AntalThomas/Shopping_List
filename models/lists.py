from db.db import sql

def all_lists():
    return sql('SELECT * FROM lists ORDER BY id')

def create_list(name):
    sql('INSERT INTO lists(name) VALUES (%s) RETURNING *', [name])

def delete_list(id):
    sql('DELETE FROM lists WHERE id=%s RETURNING *', [id])
    sql('DELETE FROM items WHERE linked_list=%s RETURNING *', [id])

def get_list(id):
    return sql('SELECT * FROM items WHERE linked_list=%s ORDER BY id', [id])

def get_list_name(id):
    return sql('SELECT * FROM lists WHERE id=%s', [id])

def make_item(name, linked_list):
    sql('INSERT INTO items(name, linked_list) VALUES (%s, %s) RETURNING *', [name, linked_list])

def delete_item(id):
    sql('DELETE FROM items WHERE id=%s RETURNING *', [id])

def item_linked_list(id):
    return sql('SELECT linked_list FROM items WHERE id=%s', [id])