from flask import Flask, request, jsonify, url_for, Blueprint
from database.db import db
from models.Users import Users, Favorites

api = Blueprint("api/users", __name__)

@api.route("/", methods=["GET"])
def get_users():
    all_users = Users.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))

    return jsonify({"all users": all_users})


@api.route("/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    single_user = Users.query.get(user_id)
    if single_user is None:
        return jsonify({"error": f"user {user_id} not found"})
    return jsonify({"user": single_user.serialize()})

@api.route("/<int:user_id>/favorites", methods=["GET"])
def get_single_user_favorites(user_id):
    single_user_favorites = Favorites.query.filter_by(users_id=user_id).all()
    return jsonify({f"user {user_id} favorites": [favorite.serialize() for favorite in single_user_favorites]})
    

@api.route("/new_user", methods=["POST"])
def new_user():
    body = request.get_json()
    new_user = Users()
    new_user.email = body["email"]
    new_user.password = body["password"]
    new_user.is_active = True

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"usuario": new_user.serialize()})

@api.route("/<int:user_id>/favorites/planet/<int:planet_id>", methods=["POST"])
def post_planets_favorites(user_id, planet_id):
    new_favorite_planet = Favorites()
    new_favorite_planet.planet_id = planet_id
    new_favorite_planet.users_id = user_id

    db.session.add(new_favorite_planet)
    db.session.commit()
    
    return jsonify({"favorite planets": new_favorite_planet.serialize()})

@api.route("/<int:user_id>/favorites/people/<int:people_id>", methods=["POST"])
def post_people_favorites(user_id, people_id):
    new_favorite_people = Favorites()
    new_favorite_people.people_id = people_id
    new_favorite_people.users_id = user_id
    db.session.add(new_favorite_people)
    db.session.commit()
    return jsonify({"favorite people": new_favorite_people.serialize()})

@api.route("/<int:user_id>/favorites/planet/<int:planet_id>", methods=["DELETE"])
def delete_planets_favorites(user_id, planet_id):
    planet_to_delete = Favorites.query.filter_by(users_id=user_id, planet_id=planet_id).first()

    if not planet_to_delete:
        return jsonify({"message": "Favorite planet not found."})
    
    db.session.delete(planet_to_delete)
    db.session.commit()

    return jsonify({"message": "planet deleted"})

@api.route("/<int:user_id>/favorites/people/<int:people_id>", methods=["DELETE"])
def delete_people_favorites(user_id, people_id):
    people_to_delete = Favorites.query.filter_by(users_id=user_id, people_id=people_id).first()

    if not people_to_delete:
        return jsonify({"message": "Favorite people not found."})
    
    db.session.delete(people_to_delete)
    db.session.commit()
    
    return jsonify({"message": "people deleted"})