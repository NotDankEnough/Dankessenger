from uuid import uuid4
from datetime import datetime

from src import socketio
from src.utils.JSONController import JSONController


@socketio.on("say")
def send_message(data):
    """The event for send message."""

    # Message timestamp:
    TIMESTAMP = datetime.timestamp(datetime.now()) * 1000

    # Message ID:
    ID = uuid4().hex

    # Returns 400 if the user tries to send a request without a name or message:
    if data is None:
        socketio.emit("message", {
            "data": None,
            "status": "You may not have filled out some fields, exceeded the limit, or not reached the minimum number of characters."
        })
        return
    
    # Message data:
    DATA = {
        "sender": {
            "username": data["sender_name"]
        },
        "message": {
            "text": data["message"],
            "timestamp": str(TIMESTAMP),
            "id": ID
        }
    }
    
    # Save the message in storage:
    if JSONController.default_type == dict: JSONController.content["messages"].append(DATA)
    elif JSONController.default_type == list: JSONController.content.append(DATA)

    JSONController.save(JSONController.latest_filepath)

    socketio.emit("message", {
        "data": DATA,
        "status": "Successfully sent the message!"
    })
