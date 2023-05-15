from dotenv import load_dotenv
load_dotenv()

import os, requests
from flask import Flask, redirect
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from routes.lists_routes import lists_routes

requests.get(f"http://omdbapi.com?apikey={os.environ.get('OMDB_API_KEY')}&t=jaws").json()
SECRET_KEY = os.environ.get("OMDB_API_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(sessions_routes, url_prefix="/sessions")
app.register_blueprint(lists_routes, url_prefix="/lists")


@app.route('/')
def index():
    return redirect('/lists')