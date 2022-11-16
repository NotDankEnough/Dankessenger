from flask_socketio import join_room

from src import socketio
from src.utils import JSONController


@socketio.on("join")
def on_connect(data) -> None:
    """The event for request to connect."""
    ROOM_ID = "xd"

    join_room(ROOM_ID)

    socketio.emit("joined", {
        "status": f"Welcome to the chat #{ROOM_ID}!",
        "chat_history": JSONController.content
    })
