import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.challenges import ticker_stream_challenge, calendar_days

logger = logging.getLogger(__name__)


@app.route('/calendarDays', methods=['POST'])
def calendar_days_all():
    data = request.get_json()
    print(data)
    output = calendar_days.calendar_days(data)
    return jsonify(output)
