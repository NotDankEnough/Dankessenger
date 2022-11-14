from .route_blueprint import blueprint
from src.utils.JSONController import JSONController

@blueprint.get("/get_messages")
def get_messages():
    """GET route for getting the messages."""
    return JSONController.content
