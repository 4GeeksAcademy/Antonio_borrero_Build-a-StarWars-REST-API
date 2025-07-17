from flask import Flask, request, jsonify, url_for, Blueprint
from models.Planets import Planets
from database.db import db

api = Blueprint("api/planets", __name__)

@api.route("/", methods=["GET"])
def get_planets():
    all_planets = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), all_planets))

    return jsonify({"all planets": all_planets})

@api.route("/<int:planet_id>", methods=["GET"])
def get_single_planet(planet_id):
    single_planet = Planets.query.get(planet_id)
    if single_planet is None:
        return jsonify({"error": f"planet {planet_id} not found"})
    return jsonify({"planet": single_planet.serialize()})

@api.route("/new_planet", methods=["POST"])
def new_planet():
    body = request.get_json()
    new_planet = Planets()
    new_planet.name = body["name"]

    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"usuario": new_planet.serialize()})