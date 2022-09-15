import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges import ticker_stream_challenge

logger = logging.getLogger(__name__)


@app.route('/tickerStreamTest', methods=['GET'])
def test():
    return "Hello, ticker stream is working"


@app.route('/tickerStreamPart1', methods=['POST'])
def ticker_stream_part_1():
    stream = request.args.get("stream")
    data = ticker_stream_challenge.to_cumulative(json.loads(stream))
    return jsonify(data)


@app.route('/tickerStreamPart2', methods=['POST'])
def ticker_stream_part_2():
    stream = request.args.get("stream")
    qty_block = request.args.get("qtyBlock")
    data = ticker_stream_challenge.to_cumulative_delayed(
        json.loads(stream), int(qty_block))
    return jsonify(data)
