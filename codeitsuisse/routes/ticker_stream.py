import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges.ticker_stream_challenge import *

logger = logging.getLogger(__name__)


@app.route('/tickerStreamTest', methods=['GET'])
def test():
    return "Hello, ticker stream is working"


@app.route('/tickerStreamPart1', methods=['POST'])
def ticker_stream_part_1():
    data = request.get_json()
    stream = data['stream']
    data = to_cumulative(stream)
    output = {"output": data}
    return jsonify(output)


@app.route('/tickerStreamPart2', methods=['POST'])
def ticker_stream_part_2():
    data = request.get_json()
    stream = data['stream']
    qty_block = int(data['quantityBlock'])
    data = to_cumulative_delayed(stream, qty_block)
    output = {"output": data}
    return jsonify(output)
