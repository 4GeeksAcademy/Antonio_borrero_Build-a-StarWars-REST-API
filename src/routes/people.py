from flask import Flask, request, jsonify, url_for, Blueprint
from database.db import db
from models.People import People

api = Blueprint("api/people", __name__)

@api.route("/", methods=["GET"])
def get_people():
    all_people = People.query.all()
    all_people = list(map(lambda x: x.serialize(), all_people))

    return jsonify({"all people": all_people})

@api.route("/<int:people_id>", methods=["GET"])
def get_single_people(people_id):
    single_people = People.query.get(people_id)
    if single_people is None:
        return jsonify({"error": f"people {people_id} not found"})
    return jsonify({"people": single_people.serialize()})

@api.route("/new_people", methods=["POST"])
def new_people():
    body = request.get_json()
    new_people = People()
    new_people.name = body["name"]

    db.session.add(new_people)
    db.session.commit()

    return jsonify({"usuario": new_people.serialize()})