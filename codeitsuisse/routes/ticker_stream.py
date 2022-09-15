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