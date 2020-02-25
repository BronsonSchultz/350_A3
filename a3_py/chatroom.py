from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class ChatForm(FlaskForm):
    """
    Flask form that allows user to send a message to a created chat room
    """
    name = ""
    message = StringField("your message")
    send = SubmitField("Send")

