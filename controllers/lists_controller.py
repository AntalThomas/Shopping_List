from flask import render_template
from services.session_info import current_user

def index():
    return render_template("lists/index.html", current_user=current_user)