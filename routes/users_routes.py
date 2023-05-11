from flask import Blueprint
from controllers.users_controller import new_user, create_users

users_routes = Blueprint('users_routes', __name__)

users_routes.route('/new')(new_user)
users_routes.route('', methods=["POST"])(create_users)