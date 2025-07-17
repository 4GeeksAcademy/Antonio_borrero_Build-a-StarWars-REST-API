from flask import Flask, request, jsonify, url_for, Blueprint
from database.db import db
from models.Users import Favorites

api = Blueprint("api/users", __name__)

@api.route("/<int:user_id>/favorites/planet/<int:planet_id>", methods=["POST"])
def post_planets_favorites(user_id, planet_id):
    new_favorite_planet = Favorites()
    new_favorite_planet.planet_id = planet_id
    new_favorite_planet.user_id = user_id
    db.session.add(new_favorite_planet)
    db.session.commit()
    return jsonify({"favorite planets": new_favorite_planet.serialize()})

@api.route("/<int:user_id>/favorites/people/<int:people_id>", methods=["POST"])
def post_planets_favorites(user_id, people_id):
    body = request.get_json()
    new_favorite_people = Favorites()
    print(new_favorite_people)
    return jsonify({"favorite people": new_favorite_people})