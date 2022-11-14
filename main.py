from flask import Flask

from src.utils.JSONController import JSONController
from src.routes.route_blueprint import blueprint

# Flask app:
app = Flask(__name__, template_folder="templates", static_folder="static")

# Load the JSON to it's controller:
JSONController.load("data.json")

# Register the routes for app:
app.register_blueprint(blueprint)
