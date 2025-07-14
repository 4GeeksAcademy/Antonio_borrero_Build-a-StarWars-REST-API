from flask import Flask, request, jsonify, url_for, Blueprint
from database.db import db
from models.Users import Users

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