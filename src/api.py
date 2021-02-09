import json
from flask import Flask

from src.setup_rolls.setup_main import setupRolls

app = Flask(__name__)

@app.route("/cats")
def cats():
    return "Cats"

@app.route("/students")
def students():
    return json.dumps(setupRolls())
