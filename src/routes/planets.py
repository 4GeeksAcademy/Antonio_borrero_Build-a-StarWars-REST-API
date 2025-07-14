from flask import Flask, request, jsonify, url_for, Blueprint
from models.Planets import Planets

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