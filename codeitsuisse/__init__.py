from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.ticker_stream
import codeitsuisse.routes.crypto_collapz
import codeitsuisse.routes.calendar_days
import codeitsuisse.routes.rubiks
import codeitsuisse.routes.travelling_suisse_robot
