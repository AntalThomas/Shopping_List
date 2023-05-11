from flask import Blueprint
from controllers.lists_controller import index

lists_routes = Blueprint("lists_routes", __name__)

lists_routes.route("")(index)