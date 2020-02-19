from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class ChatForm(FlaskForm):
    name = ''
    chat = dict()
    all_messages = list()
    message = StringField("your message")
    send = SubmitField("Send")
