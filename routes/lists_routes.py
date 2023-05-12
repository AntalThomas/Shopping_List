from flask import Blueprint
from controllers.lists_controller import index, new, create, delete, select_list, new_item, create_item, remove_item

lists_routes = Blueprint("lists_routes", __name__)

lists_routes.route("")(index)
lists_routes.route("/new")(new)
lists_routes.route("", methods=["POST"])(create)
lists_routes.route("/<id>/delete", methods=["POST"])(delete)
lists_routes.route("/<id>/list")(select_list)
lists_routes.route("/<id>/new_item")(new_item)
lists_routes.route("/<id>/list/create", methods=["POST"])(create_item)
lists_routes.route("/<id>/list/delete", methods=["POST"])(remove_item)