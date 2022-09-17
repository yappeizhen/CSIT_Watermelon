import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges.magic_cauldrons import *

logger = logging.getLogger(__name__)

@app.route('/magiccauldronsTest', methods=['GET'])
def magic_test():
    return "Hello, magiccauldrons is working"

@app.route('/magiccauldrons', methods=['POST'])
def magiccauldrons():
    data = request.get_json()
    result = []
    for input in data:
        result.append(magic_cauldrons(input))
    return jsonify(result)