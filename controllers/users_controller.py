from flask import render_template, request, redirect
from models.users import create_user

def new_user():
    return render_template("users/new.html")

def create_users():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    create_user(first_name, last_name, email, password)
    return redirect('/')