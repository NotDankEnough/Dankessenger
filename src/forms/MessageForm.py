from wtforms import Form, StringField, validators

class MessageForm(Form):
    """Message form."""

    username = StringField("username", [validators.Length(min=5, max=32)])
    """Username field."""

    message = StringField("message", [validators.Length(min=1, max=500)])
    """Message field."""
