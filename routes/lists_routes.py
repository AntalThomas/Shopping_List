from flask import Blueprint
from controllers.lists_controller import index, new, create, delete

lists_routes = Blueprint("lists_routes", __name__)

lists_routes.route("")(index)
lists_routes.route("/new")(new)
lists_routes.route("", methods=["POST"])(create)
lists_routes.route("/<id>/delete", methods=["POST"])(delete)
