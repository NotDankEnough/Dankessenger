from flask import request
from uuid import uuid4
from datetime import datetime

from .route_blueprint import blueprint
from src.forms.MessageForm import MessageForm
from src.utils.JSONController import JSONController


@blueprint.post("/send_message")
def send_message():
    """POST route for handling a send message event."""
    # Message form:
    FORM = MessageForm(request.form)

    # Message timestamp:
    TIMESTAMP = datetime.timestamp(datetime.now())

    # Message ID:
    ID = uuid4().hex

    # Returns 400 if the user tries to send a request without a name or message:
    if not FORM.validate():
        return {
            "data": None,
            "status": 400,
            "message": "Your form cannot be verified. You may not have filled out some fields, exceeded the limit, or not reached the minimum number of characters."
        }, 400
    
    # Message data:
    DATA = {
        "sender": {
            "username": FORM.username.data
        },
        "message": {
            "text": FORM.message.data,
            "timestamp": str(TIMESTAMP),
            "id": ID
        }
    }
    
    # Save the message in storage:
    JSONController.content[ID] = DATA
    JSONController.save(JSONController.latest_filepath)

    return {
        "data": DATA,
        "status": 200,
        "message": "Successfully sent the message!"
    }, 200
