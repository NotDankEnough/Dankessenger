from flask import Blueprint

blueprint = Blueprint("routes", __name__)

from .chat import chat_page
from .send_message import send_message
from .get_messages import get_messages
