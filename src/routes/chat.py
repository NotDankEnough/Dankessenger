from .route_blueprint import blueprint
from flask import render_template

@blueprint.get("/")
def chat_page():
    """GET route for chat page."""
    return render_template("form.html")
