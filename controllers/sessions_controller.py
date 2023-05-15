from flask import render_template, request, redirect, session
from models.users import find_user_by_email, remove_user
import bcrypt

def new():
    return render_template('sessions/new.html')

def create():
    email = request.form.get('email')
    password = request.form.get('password')
    user = find_user_by_email(email)

    if user == None:
        return redirect('/sessions/new')

    valid_password = bcrypt.checkpw(password.encode(), user['password_digest'].encode())
    
    if valid_password:
        session['user_id'] = int(user['id'])
        return redirect('/')
    else:
        return redirect('/sessions/new')
    
def delete():
    session.clear()
    return redirect('/')

def remove():
    remove_user(session['user_id'])
    session.clear()
    return redirect('/')