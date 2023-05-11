from flask import render_template, request, redirect
from services.session_info import current_user
from models.lists import all_lists, create_list, delete_list

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
    return redirect('/')