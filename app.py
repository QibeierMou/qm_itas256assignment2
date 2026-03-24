import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "pizza-secret-key-123"
CORS(app)

def load_init():
    """Load the init.json file for pizza types, crusts and sizes."""
    with open("static/init.json") as f:
        return json.load(f)

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=8888)