import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges import ticker_stream_challenge

logger = logging.getLogger(__name__)


@app.route('/tickerStreamTest', methods=['GET'])
def ticker_stream_test():
    return "Hello, ticker stream is working"


@app.route('/tickerStreamPart1', methods=['POST'])
def ticker_stream_part_1():
    data = request.get_json()
    stream = data['stream']
    data = ticker_stream_challenge.to_cumulative(stream)
    output = {"output": data}
    return jsonify(output)


@app.route('/tickerStreamPart2', methods=['POST'])
def ticker_stream_part_2():
    data = request.get_json()
    stream = data['stream']
    qty_block = int(data['quantityBlock'])
    data = ticker_stream_challenge.to_cumulative_delayed(stream, qty_block)
    output = {"output": data}
    return jsonify(output)
