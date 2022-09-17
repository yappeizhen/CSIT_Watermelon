import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges import rubiks_challenge

logger = logging.getLogger(__name__)


@app.route('/rubiksTest', methods=['GET'])
def rubiks_test():
    return "Hello, Rubiks is working"


@app.route('/rubiks', methods=['POST'])
def rubiks():
    data = request.get_json()
    ops = data["ops"]
    state = data["state"]
    res = rubiks_challenge.rubiks(ops, state)
    return jsonify(res)
