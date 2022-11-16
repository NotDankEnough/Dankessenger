from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO


socketio = SocketIO(cors_allowed_origins="*")
"""Websocket manager for Flask."""

def create_app() -> Flask:
    """Create a Flask application."""

    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.debug = True

    from .routes.route_blueprint import blueprint

    app.register_blueprint(blueprint)

    socketio.init_app(app)
    return app
