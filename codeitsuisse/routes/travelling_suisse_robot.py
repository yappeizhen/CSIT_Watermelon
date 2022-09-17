import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges import travelling_suisse_robot

logger = logging.getLogger(__name__)


@app.route('/travelling-suisse-robot', methods=['POST'])
def travelling_suisse_robot_method():
    data = request.get_data()
    output = travelling_suisse_robot.read_maze(data.decode())
    return jsonify(output)
