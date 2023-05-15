import os
from flask import Flask, redirect
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from routes.lists_routes import lists_routes

FLASK_SECRET_KEY = os.environ.get("SHOPPING_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(sessions_routes, url_prefix="/sessions")
app.register_blueprint(lists_routes, url_prefix="/lists")

@app.route('/')
def index():
    return redirect('/lists')