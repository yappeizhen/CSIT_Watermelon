import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges import crypto_collapz_challenge

logger = logging.getLogger(__name__)


@app.route('/cryptoCollapzTest', methods=['GET'])
def crypto_collapz_test():
    return "Hello, Crypto Collapse is working"


@app.route('/cryptocollapz', methods=['POST'])
def crypto_collapz():
    data = request.get_json()
    data = crypto_collapz_challenge.stream_crypto_collapz(data)
    return jsonify(data)
