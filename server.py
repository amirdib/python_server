import json

from bottle import Bottle

from data.access import teams, matches, stats
from utils.cors import enable_cors

app = Bottle()
app.install(enable_cors)

app.run(host='localhost', port=8080)

