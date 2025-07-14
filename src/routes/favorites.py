from flask import Flask, request, jsonify, url_for, Blueprint
from database.db import db
from models.Users import Favorites

api = Blueprint("api/users", __name__)

@api.route("/<int:user_id>/favorites", methods=["GET"])
def get_favorites(user_id):
    all_favorites = Favorites.query.all()
    all_favorites = list(map(lambda x: x.serialize(), all_favorites))

    return jsonify({"all favorites": all_favorites})