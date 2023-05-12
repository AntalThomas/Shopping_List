from db.db import sql
from flask import session

def all_lists():
    # return sql('SELECT * FROM lists ORDER BY id')
    return sql('SELECT * FROM lists WHERE linked_user=%s ORDER BY id', [session.get('user_id')])

def create_list(name, linked_user):
    sql('INSERT INTO lists(name, linked_user) VALUES (%s, %s) RETURNING *', [name, linked_user])

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