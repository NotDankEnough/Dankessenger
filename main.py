# Flask - библиотека для создания веб-сервера
from flask import Flask, request, render_template
from datetime import datetime
import json

from src.utils.clear_html_tags import clear_html_tags
from src.forms.MessageForm import MessageForm

app = Flask(__name__, template_folder="templates", static_folder="static")
DATA_FILE = "data.json"


# Загружаем сообщения из файла
def load_messages():
    with open(DATA_FILE, "r") as json_file:
        # data = {"all_messages": [] }
        data = json.load(json_file)
        return data["all_messages"]



# При старте сервераБ загружаем сообщение из файла в переменную
all_messages = load_messages()


# Сохраняем сообщение в файл
def save_messages():
    with open(DATA_FILE, "w") as json_file:
        data = {"all_messages": all_messages}
        json.dump(data, json_file)



@app.route("/")
def index():
    return render_template("form.html")


# API для получения сообщения
# /get_messages => {"messages": [...]}


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


def add_message(sender, text):
    # time: подставить автоматически
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M"),
    }
    # append - добавить элемент в список
    all_messages.append(new_message)
    save_messages()


# API для отправки соообщения
@app.post("/send_message")
def send_message():
    # Message form:
    FORM = MessageForm(request.form)

    # Returns 400 if the user tries to send a request without a name or message.
    if not FORM.validate():
        return {
            "data": None,
            "status": 400,
            "message": "Your form cannot be verified. You may not have filled out some fields, exceeded the limit, or not reached the minimum number of characters."
        }, 400

    # Save the message in storage:
    add_message(FORM.username.data, clear_html_tags(FORM.message.data))

    return {
        "data": {
            "username": FORM.username.data,
            "message": FORM.message.data
        },
        "status": 200,
        "message": "Successfully sent the message!"
    }, 200


# host 0.0.0.0 - сервер будет доступен на всех IP-адресах
# port 80 - HTTP
app.run(host="0.0.0.0", port=80)
