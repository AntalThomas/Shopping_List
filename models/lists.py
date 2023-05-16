from db.db import sql
from flask import session

def all_lists():
    return sql('SELECT * FROM lists WHERE linked_user=%s ORDER BY favourite DESC', [session.get('user_id')])

def create_list(name, linked_user, favourite):
    sql('INSERT INTO lists(name, linked_user, favourite) VALUES (%s, %s, %s) RETURNING *', [name, linked_user, favourite])

def delete_list(id):
    sql('DELETE FROM lists WHERE id=%s RETURNING *', [id])
    sql('DELETE FROM items WHERE linked_list=%s RETURNING *', [id])

def get_list(id):
    return sql('SELECT * FROM items WHERE linked_list=%s ORDER BY id', [id])

def get_list_name(id):
    return sql('SELECT * FROM lists WHERE id=%s', [id])

def make_item(name, linked_list):
    sql('INSERT INTO items(name, linked_list, linked_user) VALUES (%s, %s, %s) RETURNING *', [name, linked_list, session.get('user_id')])

def delete_item(id):
    sql('DELETE FROM items WHERE id=%s RETURNING *', [id])

def item_linked_list(id):
    return sql('SELECT linked_list FROM items WHERE id=%s', [id])

def update_item_sql(id, name):
    sql('UPDATE items SET name=%s WHERE id=%s RETURNING *', [name, id])

def get_item(id):
    items = sql('SELECT * FROM items WHERE id=%s', [id])
    return items[0]

def get_users():
    return sql('SELECT * FROM users ORDER BY first_name')

def move_item_sql(list_id, item_id):
    sql('UPDATE items SET linked_list=%s WHERE id=%s RETURNING *', [list_id, item_id])

def favourite_list_sql(id):
    list_favourite = sql('SELECT favourite FROM lists WHERE id=%s', [id])

    if list_favourite[0]['favourite'] == 0:
        sql('UPDATE lists SET favourite=%s WHERE id=%s RETURNING *', [1, id])
    else:
        sql('UPDATE lists SET favourite=%s WHERE id=%s RETURNING *', [0, id])
