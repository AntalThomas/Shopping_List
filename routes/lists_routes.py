from flask import Blueprint
from controllers.lists_controller import index, new, create, delete, select_list, new_item, create_item, remove_item, edit_item, update_item, share_list, move_item, send_item, favourite_list, crossed_off

lists_routes = Blueprint("lists_routes", __name__)

lists_routes.route("")(index)
lists_routes.route("/new")(new)
lists_routes.route("", methods=["POST"])(create)
lists_routes.route("/<id>/delete", methods=["POST"])(delete)
lists_routes.route("/<id>/list")(select_list)
lists_routes.route("/<id>/new_item")(new_item)
lists_routes.route("/<id>/list/create", methods=["POST"])(create_item)
lists_routes.route("/<id>/list/delete", methods=["POST"])(remove_item)
lists_routes.route("/<id>/edit_item.html")(edit_item)
lists_routes.route("/<id>/update_item", methods=["POST"])(update_item)
lists_routes.route("/<id>/share.html")(share_list)
lists_routes.route("/<id>/move.html")(move_item)
lists_routes.route("/<list_id>/<item_id>/send_item", methods=["POST"])(send_item)
lists_routes.route("/<id>/favourite_list", methods=["POST"])(favourite_list)
lists_routes.route("/<id>/list/crossed_off", methods=["POST"])(crossed_off)