from flask import render_template, request, redirect, session
from services.session_info import current_user
from models.lists import all_lists, create_list, delete_list, get_list, get_list_name, make_item, delete_item, item_linked_list, update_item_sql, get_item, get_users

def index():
    lists = all_lists()
    return render_template("lists/index.html", current_user=current_user, lists=lists)

def new():
    return render_template("lists/new.html")

def create():
    name = request.form.get("name")
    user_id = session.get('user_id')
    create_list(name, user_id)
    return redirect("/")

def delete(id):
    delete_list(id)
    return redirect("/")

def select_list(id):
    list = get_list(id)
    lists_name = get_list_name(id)
    return render_template("lists/list.html", list=list, lists_name=lists_name)

def new_item():
    return render_template("lists/<id>/new_item.html")

def create_item(id):
    name = request.form.get('add_item')
    make_item(name, id)
    return select_list(id)

def remove_item(id):
    lists_id = item_linked_list(id)[0]['linked_list']
    delete_item(id)
    return select_list(lists_id)

def edit_item(id):
    item = get_item(id)
    return render_template("lists/edit_item.html", item=item)

def update_item(id):
    lists_id = item_linked_list(id)[0]['linked_list']
    name = request.form.get("name")
    update_item_sql(id, name)
    return select_list(lists_id)

def share_list(id):
    all_users = get_users()
    user_id = session.get('user_id')
    return render_template("lists/share.html", all_users=all_users, user_id=user_id, list_id=id)