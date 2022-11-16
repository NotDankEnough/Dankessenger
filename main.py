from src import create_app, socketio
from src.utils import JSONController

app = create_app()

if __name__ == "__main__":
    JSONController.load("data.json", [])
    socketio.run(app)
