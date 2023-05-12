from flask import render_template, request, redirect
from services.session_info import current_user
from models.lists import all_lists, create_list, delete_list, get_list, get_list_name, make_item, delete_item, item_linked_list

def index():
    lists = all_lists()
    return render_template("lists/index.html", current_user=current_user, lists=lists)

def new():
    return render_template("lists/new.html")

def create():
    name = request.form.get("name")
    create_list(name)
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