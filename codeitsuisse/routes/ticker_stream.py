<<<<<<< HEAD
import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStreamTest', methods=['GET'])
def test():
    return "Hello, ticker stream is working"

@app.route('/tickerStreamPart1', methods=['POST'])
def ticker_stream_part_1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return json.dumps(result)
=======
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
>>>>>>> 06cc16fab376b0c10a5cbb7a8bc88b2477a75d8d
