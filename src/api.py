import json
from flask import Flask

from src.setup_rolls.setup_main import setupRolls

app = Flask(__name__)

@app.route("/cats")
def cats():
    return "cats"

@app.route("/students")
def students():
    return json.dumps(setupRolls())

# if __name__ == "__main__":
#     app.run(debug=True)