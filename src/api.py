from flask import Flask
import json

from src.main import main

app = Flask(__name__)

@app.route("/cats")
def cats():
    return "cats"

@app.route("/students")
def students():
    return json.dumps(main())

# if __name__ == "__main__":
#     app.run(debug=True)